
import pandas as pd

# 1. Load the dataset
df = pd.read_csv("Sample data (1).xlsx - Sheet1.csv")

# 2. Display the first five rows
print("First five rows:")
print(df.head())

# 3. Check the number of rows and columns
print("\nDataset shape:")
print(df.shape)

# 4. Check column names
print("\nColumn names:")
print(df.columns.tolist())

# 5. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 6. Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# 7. Check data types
print("\nData types:")
print(df.dtypes)

# ==========================================
# STEP 2: INVESTIGATE MISSING DISCOUNT BANDS
# ==========================================

print("\nMissing Discount Band records:")
print(df[df["Discount Band"].isna()][
    ["Product", "Units Sold", "Sale Price",
     "Gross Sales", "Discounts", " Sales", "Profit"]
].head(10))

print("\nDiscount values for missing Discount Band:")
print(df.loc[df["Discount Band"].isna(), "Discounts"].describe())

# ==========================================
# STEP 3: CLEAN COLUMN NAMES
# ==========================================

# Remove unwanted spaces from all column names
df.columns = df.columns.str.strip()

print("\nUpdated column names:")
print(df.columns.tolist())

# ==========================================
# STEP 4: CONVERT DATE TO DATETIME
# ==========================================

df["Date"] = pd.to_datetime(
    df["Date"],
    format="%d-%b-%y",
    errors="coerce"
)

print("\nInvalid or missing dates:", df["Date"].isna().sum())

# ==========================================
# STEP 5: VERIFY NUMERIC DATA
# ==========================================

print("\nNumeric data summary:")
print(df[["Units Sold", "Gross Sales", "Discounts",
          "Sales", "COGS", "Profit"]].describe())

# ==========================================
# STEP 6: CHECK RESULTS
# ==========================================

print("\nMissing values after initial cleaning:")
print(df.isna().sum())

print("\nDuplicate rows:", df.duplicated().sum())
print("\nData types:")
print(df.dtypes)

# ==========================================
# STEP 7: HANDLE MISSING DISCOUNT BANDS
# ==========================================

# Missing Discount Band values occur where Discounts = 0.
# Label these records explicitly rather than guessing a band.
missing_band = df["Discount Band"].isna()
zero_discount = df["Discounts"].eq(0)

df.loc[missing_band & zero_discount, "Discount Band"] = "No Discount"

# Check whether any Discount Band values remain missing
print("\nMissing values after cleaning:")
print(df.isna().sum())

# ==========================================
# STEP 8: FINAL DATA VALIDATION
# ==========================================

print("\nDuplicate rows:", df.duplicated().sum())
print("Dataset shape:", df.shape)
print("Date data type:", df["Date"].dtype)

print("\nDiscount Band counts:")
print(df["Discount Band"].value_counts(dropna=False))

# ==========================================
# STEP 9: SAVE CLEANED DATASET
# ==========================================

df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_data.csv")
