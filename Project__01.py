import pandas as pd

file_path = (r"C:\Users\hp\Downloads\Dataset for Data Analytics.xlsx")
df = pd.read_excel(file_path)

print("Excel Sheets:")
print(pd.ExcelFile(file_path).sheet_names)

print("\nFirst 5 Rows:")
print(df.head())

print("\nShape of Dataset:")
print(df.shape)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

duplicate_order_ids = df["OrderID"].duplicated().sum()
print("\nDuplicate OrderIDs:")
print(duplicate_order_ids)

duplicate_rows = df.duplicated().sum()
print("\nDuplicate Rows:")
print(duplicate_rows)

invalid_dates = df["Date"].isnull().sum()
print("\nInvalid Dates:")
print(invalid_dates)
print("\nNumeric Column Data Types:")

numeric_columns = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]
print(df[numeric_columns].dtypes)

df.to_excel("cleaned_data.xlsx", index=False)
print("\nCleaned data saved successfully!")