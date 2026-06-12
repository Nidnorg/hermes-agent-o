# © HERMÈS — SKILL: SOCIAL_CONTENT
# Agents: SURGE (social) + PULSE (influencers)
# Inspired: Fashion Nova (newsroom speed) + Luxy Hair (before/after viral)

import os, json
import anthropic

CLAUDE_KEY = os.getenv("ANTHROPIC_API_KEY")

SURGE_PROMPT = """
Tu es SURGE, agent Social Media de Veloria Hair.
Inspiré de Fashion Nova (speed) et Luxy Hair (avant/après viral).
Crée des hooks tiktok/reels : hook 2 premières secondes, transformation visible, CTA final.
Emojis stratégiques. Max 5 hashtags pertinents.
Français. Max 5 idées par appel.
"""

def skill_generate_social_content(product: str, platform: str = "TikTok", count: int = 5) -> list:
    """Génère des idées de contenu pour TikTok/Instagram"""
    client = anthropic.Anthropic(api_key=CLAUDE_KEY)
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=800,
        system=SURGE_PROMPT,
        messages=[{
            "role":"user",
            "content": f"Genère {count} idées {platform} pour : {product}. Retourne JSON liste de {{hook,script,caption,hashtags}}"
        }]
    )
    text = msg.content[0].text.strip()
    if text.startswith("```"): text = text.split("\n",1)[1].rsplit("```",1)[0]
    try: return json.loads(text)
    except: return [{"content": text}]

def skill_influencer_brief(product: str, niche: str = "beauté") -> str:
    """PULSE : gen brief influenceur"""
    client = anthropic.Anthropic(api_key=CLAUDE_KEY)
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=600,
        system="Tu es PULSE, agent Influence de Veloria Hair. Gens des briefs micro-influenceurs gifting. But : contenu UGC gratuit.",
        messages=[{"role":"user","content":f"Brief influenceur {niche} pour {product}. Gifting gratuit."}]
    )
    return msg.content[0].text