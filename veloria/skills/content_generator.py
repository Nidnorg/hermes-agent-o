# © HERMÈS — SKILL: CONTENT_GENERATOR
# Agents: NOVA (copy) + SCRIBE (blog)
# Inspired by: Kylie Cosmetics (luxury copy) + Luxy Hair (educational)

import os, anthropic

CLAUDE_KEY = os.getenv("ANTHROPIC_API_KEY")

NOVA_PROMPT = """
Tu es NOVA, copywriter premium de Veloria Hair.
Style Kylie Cosmetics : luxueux, exclusif, urgent.
Remarque : bénéfice > feature. transformation > produit. CTA urgent.
Français. Max 200 mots.
"""

SCRIBE_PROMPT = """
Tu es SCRIBE, agent Blog de Veloria Hair.
Inspis� de Luxy Hair : contenu éducatif qui génère du trafic organique massif.
Articles SEO-friendly sur les extensions RAW.
Français. Max 600 mots.
"""

def skill_generate_product_description(product: str, origin: str, length: str) -> str:
    client = anthropic.Anthropic(api_key=CLAUDE_KEY)
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=600,
        system=NOVA_PROMPT,
        messages=[{"role":"user","content":f"Description premium pour : {product} | {origin} | {length}"}]
    )
    return msg.content[0].text

def skill_generate_blog_article(topic: str) -> str:
    client = anthropic.Anthropic(api_key=CLAUDE_KEY)
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1200,
        system=SCRIBE_PROMPT,
        messages=[{"role":"user","content":f"Article blog SEO sur : {topic}"}]
    )
    return msg.content[0].text