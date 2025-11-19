import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ✅ 1. Page setup
st.set_page_config(page_title="Veg & Fruit Prices Dashboard", layout="wide")
st.title("🥦 Vegetable & Fruit Prices Dashboard")
st.markdown("Visual dashboard to explore historical prices of vegetables and fruits across Indian markets.")

# ✅ 2. Load data
df = pd.read_csv("Veg_fruits_price_India.csv")
df.columns = df.columns.str.strip()  # Remove spaces from column names

# ✅ 3. Handle date and price columns
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df = df.dropna(subset=["Date", "price"])

# ✅ 4. Sidebar filters
st.sidebar.header("🔍 Filter Options")
items = st.sidebar.multiselect(
    "Select Items",
    sorted(df["Item Name"].dropna().unique()),
    default=sorted(df["Item Name"].dropna().unique())[:3]  # choose first 3 valid items
)

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["Date"].min(), df["Date"].max()]
)

# ✅ 5. Filter the data
filtered_df = df[
    (df["Item Name"].isin(items)) &
    (df["Date"] >= pd.to_datetime(date_range[0])) &
    (df["Date"] <= pd.to_datetime(date_range[1]))
]

# ✅ 6. Show table
st.subheader("📄 Filtered Data Table")
st.dataframe(filtered_df)

# ✅ 7. Summary statistics
st.subheader("📌 Summary Statistics")
if not filtered_df.empty:
    col1, col2, col3 = st.columns(3)
    col1.metric("📉 Min Price", f"₹{filtered_df['price'].min():.2f}")
    col2.metric("📈 Max Price", f"₹{filtered_df['price'].max():.2f}")
    col3.metric("📊 Avg Price", f"₹{filtered_df['price'].mean():.2f}")
else:
    st.warning("No data available for selected filters.")

# ✅ 8. Line chart
st.subheader("📈 Price Trend Over Time")
for item in items:
    item_data = filtered_df[filtered_df["Item Name"] == item]
    if not item_data.empty:
        st.line_chart(item_data.set_index("Date")["price"])

# ✅ 9. Bar chart
st.subheader("📊 Average Price Comparison")
avg_price = filtered_df.groupby("Item Name")["price"].mean().reset_index()
if not avg_price.empty:
    st.bar_chart(avg_price.set_index("Item Name"))
else:
    st.info("No data to show.")
