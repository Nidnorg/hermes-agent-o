#!/usr/bin/env python3
"""
⚡ HERMÈS — ECOM AGENT IMPORTER
Fork de : github.com/skypank-coder/Ecom-agent
Agent : VAULT + CHAIN
Mission : Importer les produits K-Hair Factory → Shopify Veloria en < 20 secondes
"""

import os, json, requests, anthropic
from playwright.sync_api import sync_playwright

SHOPIFY_STORE = os.getenv("SHOPIFY_STORE", "veloriahair.myshopify.com")
SHOPIFY_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
CLAUDE_KEY    = os.getenv("ANTHROPIC_API_KEY")

SUPPLIER_URLS = [
    "https://k-hair.com/product/raw-straight-hair/",
    "https://apohair.com/raw-straight-hair-extensions/",
    "https://unihairvn.com/raw-straight-hair/"
]

def scrape_supplier_page(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle", timeout=30000)
        text = page.inner_text("body")
        browser.close()
    return text[:8000]

def extract_product_data(raw_text: str) -> dict:
    client = anthropic.Anthropic(api_key=CLAUDE_KEY)
    prompt = f"""
Tu es VAULT, agent Stock de Veloria Hair. Extrais les données produit de ce texte fournisseur.
Retourne UNIQUEMENT du JSON valide avec cette structure exacte :
{{
  "title": "Veloria | [Origine] RAW Straight Hair — Grade 12A Premium",
  "body_html": "<description luxueuse en français>",
  "vendor": "Veloria Hair",
  "product_type": "Hair Extensions",
  "tags": ["raw hair", "premium", "straight", "vietnamese hair"],
  "variants": [
    {{"title": "22 inches", "price": "149.00", "sku": "VH-ST-22"}},
    {{"title": "24 inches", "price": "175.00", "sku": "VH-ST-24"}},
    {{"title": "26 inches", "price": "199.00", "sku": "VH-ST-26"}},
    {{"title": "28 inches", "price": "229.00", "sku": "VH-ST-28"}},
    {{"title": "30 inches", "price": "259.00", "sku": "VH-ST-30"}}
  ]
}}

Texte fournisseur : {raw_text}
"""
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )
    text = msg.content[0].text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(text)

def publish_to_shopify(product_data: dict) -> dict:
    headers = {
        "X-Shopify-Access-Token": SHOPIFY_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {"product": {**product_data, "status": "draft"}}
    r = requests.post(
        f"https://{SHOPIFY_STORE}/admin/api/2024-10/products.json",
        json=payload, headers=headers
    )
    return r.json()

def import_from_supplier(url: str) -> dict:
    """Pipeline complet : URL fournisseur → Shopify Veloria en < 20 secondes"""
    import time
    start = time.time()
    print(f"\n🔍 Scraping : {url}")
    raw = scrape_supplier_page(url)
    print(f"📦 Extraction données produit...")
    data = extract_product_data(raw)
    print(f"🚀 Publication sur Shopify...")
    result = publish_to_shopify(data)
    elapsed = round(time.time() - start, 1)
    print(f"✅ Importé en {elapsed}s : {data.get('title', 'N/A')}")
    return {"success": True, "time": elapsed, "product": data.get("title"), "shopify": result}

if __name__ == "__main__":
    print("⚡ HERMÈS — Ecom Agent Importer")
    print("Agents : VAULT + CHAIN")
    print(f"Fournisseurs configurés : {len(SUPPLIER_URLS)}")
    # Test sur K-Hair
    # result = import_from_supplier(SUPPLIER_URLS[0])
    # print(json.dumps(result, indent=2, ensure_ascii=False))
