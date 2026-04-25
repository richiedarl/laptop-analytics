# scripts/generate_data.py

import pandas as pd
from faker import Faker
from datetime import timedelta
import random
import os

fake = Faker()

# =========================
# CONFIGURATION
# =========================

NUM_LAPTOPS = 200
NUM_EMPLOYEES = 150

MODELS = ["Dell Latitude", "HP EliteBook", "Lenovo ThinkPad", "MacBook Pro", "Acer Aspire"]

VENDORS = ["Dell NG", "HP Africa", "Lenovo West Africa", "TechSupply Ltd", "Prime Devices"]

DEPARTMENTS = ["IT", "HR", "Finance", "Operations", "Admin", "Engineering"]

BRANCHES = ["Lagos HQ", "Abuja Office", "Port Harcourt Branch", "Ibadan Office", "Enugu Branch"]

ISSUE_TYPES = ["Battery Failure", "Screen Damage", "Keyboard Fault", "Overheating", "Charging Port Issue"]

STATUSES = ["Assigned", "Returned", "Damaged"]

# =========================
# PATH SETUP (FIXED ONCE ONLY)
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# 1. GENERATE LAPTOPS
# =========================

laptops = []

for i in range(1, NUM_LAPTOPS + 1):
    purchase_date = fake.date_between(start_date='-2y', end_date='today')
    warranty_expiry = purchase_date + timedelta(days=365 * 2)

    laptops.append({
        "laptop_id": i,
        "model": random.choice(MODELS),
        "vendor": random.choice(VENDORS),
        "purchase_cost": random.randint(250000, 850000),
        "purchase_date": purchase_date,
        "warranty_expiry": warranty_expiry
    })

laptops_df = pd.DataFrame(laptops)

laptops_df.to_csv(os.path.join(OUTPUT_DIR, "laptops.csv"), index=False)

print("laptops.csv created successfully")

# =========================
# 2. GENERATE ASSIGNMENTS
# =========================

assignments = []

for i in range(1, NUM_EMPLOYEES + 1):
    assignments.append({
        "assignment_id": i,
        "laptop_id": random.randint(1, NUM_LAPTOPS),
        "staff_name": fake.name(),
        "department": random.choice(DEPARTMENTS),
        "branch": random.choice(BRANCHES),
        "status": random.choice(STATUSES),
        "assigned_date": fake.date_between(start_date='-1y', end_date='today')
    })

assignments_df = pd.DataFrame(assignments)

assignments_df.to_csv(os.path.join(OUTPUT_DIR, "distributions.csv"), index=False)

print("distributions.csv created successfully")

# =========================
# 3. GENERATE REPAIRS
# =========================

repairs = []

for i in range(1, 101):
    repairs.append({
        "repair_id": i,
        "laptop_id": random.randint(1, NUM_LAPTOPS),
        "issue_type": random.choice(ISSUE_TYPES),
        "repair_cost": random.randint(10000, 120000),
        "repair_date": fake.date_between(start_date='-1y', end_date='today')
    })

repairs_df = pd.DataFrame(repairs)

repairs_df.to_csv(os.path.join(OUTPUT_DIR, "repairs.csv"), index=False)

print("repairs.csv created successfully")

# =========================
# 4. GENERATE VENDORS
# =========================

vendors_data = []

for i, vendor in enumerate(VENDORS, start=1):
    vendors_data.append({
        "vendor_id": i,
        "vendor_name": vendor,
        "avg_delivery_days": random.randint(2, 14),
        "defect_rate": round(random.uniform(1.0, 8.5), 2)
    })

vendors_df = pd.DataFrame(vendors_data)

vendors_df.to_csv(os.path.join(OUTPUT_DIR, "vendors.csv"), index=False)

print("vendors.csv created successfully")

print("\nAll CSV files generated successfully inside /output folder")