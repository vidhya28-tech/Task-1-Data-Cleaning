import pandas as pd

# Load raw dataset
df = pd.read_csv("data/marketing_campaign_raw.csv")

# Clean column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

# Standardize text
for col in ["education", "marital_status"]:
    df[col] = df[col].astype("string").str.strip()

df["marital_status"] = df["marital_status"].replace({
    "Alone": "Single",
    "Absurd": "Other",
    "YOLO": "Other"
})

# Handle missing income values with the median
df["income"] = df["income"].fillna(df["income"].median())

# Remove exact duplicate rows
df = df.drop_duplicates().reset_index(drop=True)

# Convert date and standardize the display format
df["dt_customer"] = pd.to_datetime(
    df["dt_customer"], format="%d-%m-%Y", errors="coerce"
)
df["dt_customer"] = df["dt_customer"].dt.strftime("%d-%m-%Y")

# Convert other columns to numeric where appropriate
numeric_cols = [
    c for c in df.columns
    if c not in ["education", "marital_status", "dt_customer"]
]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.to_csv("data/marketing_campaign_cleaned.csv", index=False)
print("Cleaning complete.")
print("Cleaned shape:", df.shape)
