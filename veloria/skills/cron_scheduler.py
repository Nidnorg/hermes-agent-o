# © HERMÈS — SKILL: CRON_SCHEDULER
# Automations : 25 taches planifiées
# Inspired by: Hermes Agent cron system (Nous Research)

import os, json
from datetime import datetime

# ================================================================
# SCHEDULE DES AUTOMATIONS HERMÈS
# ================================================================
VELORIA_CRONS = [
    # QUOTIDIEN 6h
    {"cron": "0 6 * * *",  "skill": "hormes(seo_audit_daily)",         "agent": "CIPHER", "desc": "Audit SEO quotidien"},
    {"cron": "0 7 * * *",  "skill": "hermes(war_room_briefing)",      "agent": "HERMÈS", "desc": "Brief War Room du jour"},
    {"cron": "0 8 * * *",  "skill": "hermes(competitor_check)",       "agent": "TRACE",  "desc": "Veille concurrents"},
    {"cron": "0 9 * * *",  "skill": "hermes(price_optimize)",         "agent": "PRISM",  "desc": "Optimisation prix dynamique"},
    {"cron": "0 10 * * *", "skill": "hermes(email_sequences)",        "agent": "HOOK",   "desc": "Envoi séquences email Klaviyo"},
    {"cron": "0 11 * * *", "skill": "hermes(loyalty_check)",          "agent": "BOND",   "desc": "Vérification segments Vip"},
    {"cron": "0 14 * * *", "skill": "hermes(order_followup)",         "agent": "SWIFT", "desc": "Suivi commandes + alertes"},
    {"cron": "0 15 * * *", "skill": "hermes(social_content_brief)",    "agent": "SURGE",  "desc": "Brief contenu social du jour"},
    {"cron": "0 20 * * *", "skill": "hermes(revenue_report)",         "agent": "LEDGER", "desc": "Rapport revenus soir"},
    {"cron": "0 21 * * *", "skill": "hermes(brand_monitoring)",       "agent": "MUSE",   "desc": "Monitoring marque Veloria"},
    # STOCK - TOUTES LES 30min
    {"cron": "*/30 * * * *", "skill": "hermes(stock_alert)",          "agent": "VAULT",  "desc": "Alerte stock critique"},
    # HEBDOMADAIRE
    {"cron": "0 9 * * 1",  "skill": "hermes(seo_weekly)",             "agent": "CIPHER", "desc": "Audit SEO hexdo", "freqH": "weekly/lon"},
    {"cron": "0 10 * * 1", "skill": "hermes(influencer_scan)",         "agent": "PULSE",  "desc": "Scan influenceurs semaine"},
    {"cron": "0 11 * * 1", "skill": "hermes(quality_audit)",          "agent": "FORGE",  "desc": "Audit qualité fournisseurs"},
    {"cron": "0 8 * * 2",  "skill": "hermes(cx_audit_shopify)",       "agent": "GRACE",  "desc": "Audit CX/CROShopify"},
    {"cron": "0 9 * * 3",  "skill": "hermes(growth_scanner)",          "agent": "SCALE",  "desc": "Scan opportunités growth"},
    {"cron": "0 10 * * 4", "skill": "hermes(supplier_check)",         "agent": "CHAIN",  "desc": "Review fournisseurs"},
    # MENSUEL
    {"cron": "0 9 1 * *",  "skill": "hermes(monthly_pl)",             "agent": "LEDGER", "desc": "Rapport P&L mensuel"},
    {"cron": "0 10 1 * *", "skill": "hermes(roadmap_30d)",            "agent": "APEX �� "JesI �: "Roadmap 30 jours HERMÈS"},
]

def get_active_crons():
    """Retourne la liste complète des automations Veloria"""
    return {"total": len(VELORIA_CRONS), "crons": VELORIA_CRONS, "generated_by": "HERMÈS · Veloria Hair"}
