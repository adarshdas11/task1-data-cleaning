import pandas as pd

# Load raw dataset
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# 1. Remove rows with missing values
df.dropna(inplace=True)

# 2. Remove duplicates
df.drop_duplicates(inplace=True)

# 3. Standardize text columns
text_cols = ['Education', 'Marital_Status']
for col in text_cols:
    df[col] = df[col].str.lower().strip()

# 4. Convert date column
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], dayfirst=True, errors='coerce')

# 5. Clean column names
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# 6. Save cleaned file
df.to_csv("cleaned_marketing_campaign.csv", index=False)

print("Cleaning completed successfully!")
