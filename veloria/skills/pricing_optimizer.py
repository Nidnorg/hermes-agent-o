# © HERMÈS — SKILL: PRICING_OPTIMIZER
# Agent: PRISM
# Inspired: SKIMS (scarcity pricing) + kylie (drops 48h) + pricing-decision-agent

import os, json
import anthropic

CLAUDE_KEY = os.getenv("ANTHROPIC_API_KEY")

# Pricing psychologique Veloria - Grille de base
BASE_PRICING = {
    "22": 149.00, "24": 175.00, "26": 199.00, "28": 229.00, "30": 259.00
}

def skill_pricing_psychology(price: float) -> float:
    """Convertit un prix en prix psychologique"""
    import math
    base = math.floor(price)
    if base % 10 == 0: return float(base - 1)  # 150 -> 149
    return float(base)

def skill_generate_drop_pricing(lengths: list, drop_duration_h = 48) -> dict:
    """PRISM : génère les prix pour un drop limité style Kylie"""
    result = {
        "drop_duration_h": drop_duration_h,
        "scarcity_message": "⚠ Édition limitée — Disponible 48h seulement",
        "variants": []
    }
    for length in lengths:
        base_p = BASE_PRICING.get(str(length), 199)
        result["variants"].append({
            "length": f"{length}\"",
            "price": skill_pricing_psychology(base_p),
            "compare_at_price": round(base_p * 1.2, 2),
            "stock_message": "Plus que 3 en stock",
            "urgency": f"Offre expire dans {drop_duration_h}h"
        })
    return result

def skill_bundle_pricing(items: list) -> dict:
    """PRISM : bundle + 30% panier moyen"""
    individual_total = sum(i.get("price", 0) for i in items)
    bundle_price = skill_pricing_psychology(individual_total * 0.85)
    return {
        "bundle_price": bundle_price,
        "individual_total": individual_total,
        "discount": round((1 - bundle_price / individual_total) * 100, 1),
        "savings_message": f"ÉConomisez {round(individual_total - bundle_price, 2)}€ en l'achetant ensemble"
    }