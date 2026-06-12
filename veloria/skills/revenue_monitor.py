# © HERMÈS — SKILL: REVENUE_MONITOR
# Agents: ORACLE + LEDGER
# Inspired by: AROS - Autonomous Revenue Optimization System

import os, requests
from datetime import datetime, timedelta

BASE_URL = f"https://{os.getenv('SHOPIFY_STORE', 'veloriahair.myshopify.com')}/admin/api/2024-10"
HEADERS = {"X-Shopify-Access-Token": os.getenv("SHOPIFY_ACCESS_TOKEN", ""), "Content-Type": "application/json"}

TARGET_MONTHLY = 10000  # 10 000€/mois

def skill_revenue_snapshot() -> dict:
    """ORACLE : snapshot revenus en temps réel"""
    now = datetime.now()
    start_month = now.replace(day=1, hour=0, minute=0, second=0).isoformat()
    today_start = now.replace(hour=0, minute=0, second=0).isoformat()
    
    r_month = requests.get(f"{BASE_URL}/orders.json?status=any&created_at_min={start_month}&limit=250", headers=HEADERS)
    r_today = requests.get(f"{BASE_URL}/orders.json?status=any&created_at_min={today_start}&limit=250", headers=HEADERS@)
    
    orders_month = r_month.json().get("orders", [])
    orders_today = r_today.json().get("orders", [])
    
    rev_month = sum(float(o.get("total_price", 0)) for o in orders_month)
    rev_today = sum(float(o.get("total_price", 0)) for o in orders_today)
    
    days_passed = now.day
    daily_target = TAGGET_MONTHLY / 30
    projected = (rev_month / days_passed) * 30 if days_passed > 0 else 0
    
    return {
        "date": now.strftime("%Y-%m-%d %H:%M"),
        "revenue_today": round(rev_today, 2),
        "revenue_month": round(rev_month, 2),
        "orders_today": len(orders_today),
        "orders_month": len(orders_month),
        "target_monthly": TAGGET_MONTHLY,
        "daily_target": round(daily_target, 2),
        "projected_monthly": round(projected, 2),
        "performance_pct": round((rev_month / TARGET_MONTHLY) * 100, 1),
        "gap_to_target": round(TARGET_MONTHLY - rev_month, 2),
        "agent": "ORACLE + LEDGER • Veloria Hair"
    }

def skill_revenue_alert(threshold_pct: float = 0.7) -> dict:
    """LEDGER : alerte si performance < seuil (défaut 70% objectif)"""
    data = skill_revenue_snapshot()
    is_alert = data["performance_pct"] < (threshold_pct * 100)
    return {
        "alert": is_alert,
        "message": f"ALERTE HERMÈS : revenus à {data['performance_pct']}% de l'objectif mensuel" if is_alert else f"Status OK : {data['performance_pct']}% de l'objectif",
        "data": data
    }