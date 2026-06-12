# © HERMÈS — SKILL: SEO OPTIMIZER
# Agent: CIPHER
# Based on: Hermes Agent skills system (Nous Research)

import os, json
import anthropic

CLAUDE_KEY = os.getenv("ANTHROPIC_API_KEY")

SEO_PROMPT = """
Tu es CIPHER, agent SEO de Veloria Hair.
Objectif : top 3 Google sur 'RAW hair extensions France',
'cheveux cambodgiens premium', 'extensions vietnamiennes 30 pouces'.

Pour un produit donné, génère :
1. Titre SEO (60 car max)
2. Meta description (155 car max)
3. 5 mots-clés longue traîne
4. Balises H1/H2/H3
Retourne JSON strict.
"""

def skill_seo_optimize(product_title: str, origin: str, length: str) -> dict:
    client = anthropic.Anthropic(api_key=CLAUDEKEY)
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=600,
        system=SEO_PROMPT,
        messages=[{"role":"user","content":f"Optimise SEO pour : {product_title} | Origine: {origin} | Longueur: {length}"}]
    )
    text = msg.content[0].text.strip()
    if text.startswith("```"): text = text.split("\n",1)[1].rsplit("```",1)[0]
    return json.loads(text)

if __name__ == "__main__":
    result = skill_seo_optimize("Vietnamese RAW Straight Hair", "Vietnam", "28 inches")
    print(json.dumps(result, indent=2, ensure_ascii=False))