from sqlalchemy import create_engine
from urllib.parse import quote_plus

import pandas as pd

raw_password = "Realwealthyandtea"
encoded_password = quote_plus(raw_password)

DATABASE_URL = f"postgresql://postgres.jcydwwkohqpmfepgztzq:{encoded_password}@aws-0-eu-west-1.pooler.supabase.com:6543/postgres"

engine = create_engine(DATABASE_URL)


# Load CSVs
laptops = pd.read_csv("output/laptops.csv")
distributions = pd.read_csv("output/distributions.csv")
repairs = pd.read_csv("output/repairs.csv")
vendors = pd.read_csv("output/vendors.csv")

# Push to database
laptops.to_sql("laptops", engine, if_exists="replace", index=False)
distributions.to_sql("distributions", engine, if_exists="replace", index=False)
repairs.to_sql("repairs", engine, if_exists="replace", index=False)
vendors.to_sql("vendors", engine, if_exists="replace", index=False)

print("Upload complete")