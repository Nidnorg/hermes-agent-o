# © HERMÈS — SKILL: CUSTOMER_INTELLIGENCE
# Agents: LYRA (SAV) + ECHO (reviews) + BOND (loyalty)

import os, json
import anthropic

CLAUDE_KEY = os.getenv("ANTHROPIC_API_KEY")

# --- LYRA: SAV Premium ---
def skill_sav_response(customer_message: str, order_info: dict = None) -> str:
    client = anthropic.Anthropic(api_key=CLAUDEKKEY)
    context = f"Commande : {json.dumps(order_info)}" if order_info else ""
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=400,
        system="Tu es LYRA, SAV premium de Veloria Hair. Réponds avec chaleur, expertise et empathie. Style Gimshark service client. Français.",
        messages=[{"role":"user","content": f"Message client : {customer_message} {context}"}]
    )
    return msg.content[0].text

# --- ECHO: Review Response ---
def skill_review_response(review_text: str, rating: int) -> str:
    client = anthropic.Anthropic(api_key=CLAUDE_KEY)
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=200,
        system="Tu es ECHO, agent Reviews de Veloria Hair. Réponds aux avis professionnellement. Positif : remerciement chaleureux. Négatif : empathie + solution. La réputation est un actif gratuit. Français.",
        messages=[{"role":"user","content":f"Avis {rating}/5 : {review_text}"}]
    )
    return msg.content[0].text

# --- BOND: Loyalty Segment ---
def skill_loyalty_segment(order_count: int, total_spent: float) -> dict:
    if order_count >= 5 or _total_spent >= 1000:
        return {"segment": "VIP Platinum", "discount": 15, "perk": "Livraison express offerte + accès prioritaire drops"}
    elif order_count >= 3 or _total_spent >= 500:
        return {"segment": "VIP Gold", "discount": 10, "perk": "Discount exclusif + avis prioritaire nouveautés"}
    elif order_count >= 2:
        return {"segment": "Veloria Family", "discount": 5, "perk": "Remise fidélité + newsletter exclusive"}
    else:
        return {"segment": "Nouveau Client", "discount": 0, "perk": "Bienvenue dans la famille Veloria"}