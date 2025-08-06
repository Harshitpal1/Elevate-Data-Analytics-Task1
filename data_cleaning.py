# Elevate Data Analyst Internship - Task 1: Data Cleaning and Preprocessing
# This script cleans the 'Customer Personality Analysis' dataset.
 
#  Step 1: Import necessary libraries ---
import pandas as pd
from datetime import datetime

print("Starting the data cleaning process...")

#  Step 2: Load the dataset ---
# The dataset is tab-separated, so we use sep='\t'.
try:
    data = pd.read_csv('marketing_campaign.csv', sep='\t')
    print("✅ Dataset loaded successfully.")
    print(f"   Initial shape: {data.shape[0]} rows, {data.shape[1]} columns")
except FileNotFoundError:
    print("❌ Error: 'marketing_campaign.csv' not found.")
    print("   Please ensure the file is in the same directory as this script.")
    exit()

#  Step 3: Rename columns for consistency ---
# We make column names lowercase and use underscores.
data.rename(columns={
    'ID': 'id',
    'Year_Birth': 'year_birth',
    'Education': 'education',
    'Marital_Status': 'marital_status',
    'Income': 'income',
    'Kidhome': 'kid_home',
    'Teenhome': 'teen_home',
    'Dt_Customer': 'dt_customer',
    'Recency': 'recency',
    'MntWines': 'mnt_wines',
    'MntFruits': 'mnt_fruits',
    'MntMeatProducts': 'mnt_meat',
    'MntFishProducts': 'mnt_fish',
    'MntSweetProducts': 'mnt_sweet',
    'MntGoldProds': 'mnt_gold',
    'NumDealsPurchases': 'num_deals_purchases',
    'NumWebPurchases': 'num_web_purchases',
    'NumCatalogPurchases': 'num_catalog_purchases',
    'NumStorePurchases': 'num_store_purchases',
    'NumWebVisitsMonth': 'num_web_visits_month'
}, inplace=True)
print("✅ Columns renamed.")

#  Step 4: Handle missing values ---
# The 'income' column has missing values. We fill them with the median.
missing_before = data['income'].isnull().sum()
if missing_before > 0:
    median_income = data['income'].median()
    data['income'].fillna(median_income, inplace=True)
    print(f"✅ Filled {missing_before} missing income values with the median ({median_income}).")
else:
    print("✅ No missing income values found.")

#  Step 5: Convert data types and create new features ---
# Convert date column and create 'age' and 'total_children' features.
data['dt_customer'] = pd.to_datetime(data['dt_customer'], dayfirst=True)
data['age'] = datetime.now().year - data['year_birth']
data['total_children'] = data['kid_home'] + data['teen_home']
print("✅ Converted 'dt_customer' to datetime and created 'age' and 'total_children' features.")

#  Step 6: Standardize categorical values ---
# Group inconsistent marital status values.
data['marital_status'] = data['marital_status'].replace({
    'Married': 'Partner',
    'Together': 'Partner',
    'Absurd': 'Single',
    'Widow': 'Single',
    'YOLO': 'Single',
    'Divorced': 'Single',
    'Alone': 'Single'
})
print("✅ Standardized 'marital_status' values.")

#  Step 7: Remove duplicate rows ---
initial_rows = data.shape[0]
data.drop_duplicates(inplace=True)
duplicates_removed = initial_rows - data.shape[0]
if duplicates_removed > 0:
    print(f"✅ Removed {duplicates_removed} duplicate rows.")
else:
    print("✅ No duplicate rows found.")

#  Step 8: Perform basic outlier treatment ---
initial_rows = data.shape[0]
data = data[(data['age'] < 90) & (data['income'] < 250000)]
outliers_removed = initial_rows - data.shape[0]
if outliers_removed > 0:
    print(f"✅ Removed {outliers_removed} outlier rows (age > 90 or income > 250k).")
else:
    print("✅ No outliers found based on current filters.")

#  Step 9: Final check and save the cleaned data ---
print("\n--- Final Cleaned Data Info ---")
data.info()

# Save the cleaned data to a new CSV file
try:
    data.to_csv('cleaned_customer_data.csv', index=False)
    print("\n🚀 Success! Cleaned data has been saved to 'cleaned_customer_data.csv'")
except Exception as e:
    print(f"\n❌ Error saving file: {e}")


