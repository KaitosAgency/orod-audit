# -*- coding: utf-8 -*-
"""Télécharge des fiches produit orod.fr et résume les attributs alt des images."""

from __future__ import annotations

import json
import re
import ssl
import time
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

BASE = "https://orod.fr"
SITEMAP = BASE + "/sitemap.xml"
OUT_DIR = Path(__file__).resolve().parent.parent / "audit-complet" / "references" / "produits-crawl"
SUMMARY_JSON = OUT_DIR / "resume-images-alt.json"
USER_AGENT = "Mozilla/5.0 (compatible; OrodAuditBot/1.0; +https://orod.fr)"


def fetch(url: str, timeout: int = 45) -> bytes:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, context=ctx, timeout=timeout) as r:
        return r.read()


def looks_like_product_path(path: str) -> bool:
    """Heuristique: URL liste dans le sitemap pour les produits (suffixe réf ou préfixe numérique)."""
    slug = path.rstrip("/").split("/")[-1]
    if not slug or slug in ("fr",):
        return False
    # ex: aerosol-decontaminant-50ml-019284
    if re.search(r"-\d{5,}$", slug):
        return True
    # ex: 580460-medaille-...-4851102
    if re.match(r"^\d{4,}-", slug):
        return True
    return False


def safe_filename(url: str) -> str:
    p = urlparse(url).path.strip("/").replace("/", "_")
    if len(p) > 120:
        p = p[:120]
    return p + ".html"


def analyze_images(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for img in soup.find_all("img"):
        alt = img.get("alt")
        rows.append(
            {
                "src": (img.get("src") or "")[:200],
                "alt_present": alt is not None,
                "alt_empty": alt is not None and str(alt).strip() == "",
                "alt_value": (str(alt)[:120] if alt is not None else None),
            }
        )
    return rows


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    xml = fetch(SITEMAP).decode("utf-8", "replace")
    locs = re.findall(r"<loc>\s*(https://orod\.fr[^<\s]+)\s*</loc>", xml)
    product_urls = []
    seen = set()
    for u in locs:
        path = urlparse(u).path
        if path == "/" or path == "":
            continue
        if not looks_like_product_path(path):
            continue
        if u in seen:
            continue
        seen.add(u)
        product_urls.append(u)

    # Varier un peu : quelques URLs en début / milieu du sitemap
    pick = []
    last_idx = max(0, len(product_urls) - 1)
    indices = [0, 1, 2, 5, 10, 25, 50, min(80, last_idx)]
    for i in indices:
        if i < len(product_urls) and product_urls[i] not in pick:
            pick.append(product_urls[i])
    for u in product_urls:
        if len(pick) >= 10:
            break
        if u not in pick:
            pick.append(u)

    summary = {"sources": {}, "urls": [], "counts": {}}

    for url in pick:
        time.sleep(0.35)
        try:
            body = fetch(url).decode("utf-8", "replace")
        except Exception as e:
            summary["counts"][url] = {"error": str(e)}
            continue
        fn = OUT_DIR / safe_filename(url)
        fn.write_text(body, encoding="utf-8")
        imgs = analyze_images(body)
        total = len(imgs)
        no_alt_attr = sum(1 for x in imgs if not x["alt_present"])
        empty_alt = sum(1 for x in imgs if x["alt_empty"])
        filled = sum(1 for x in imgs if x["alt_present"] and not x["alt_empty"])
        summary["urls"].append(url)
        summary["counts"][url] = {
            "file": str(fn.name),
            "img_total": total,
            "img_without_alt_attr": no_alt_attr,
            "img_alt_empty": empty_alt,
            "img_alt_filled": filled,
        }
        summary["sources"][url] = imgs[:40]

    SUMMARY_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print("OK", len(pick), "pages")
    print("Dossier:", OUT_DIR)
    print("Résumé:", SUMMARY_JSON)


if __name__ == "__main__":
    main()
