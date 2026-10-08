import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="E-Commerce Dashboard",
    page_icon="📊",
    layout="wide"
)

DATA_DIR = Path("dashboard_data")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_DIR / "dashboard_data.csv")
    monthly = pd.read_csv(DATA_DIR / "monthly_sales.csv")
    category = pd.read_csv(DATA_DIR / "category_sales.csv")
    delivery = pd.read_csv(DATA_DIR / "delivery_review.csv")
    return df, monthly, category, delivery

df, monthly, category, delivery = load_data()

df["order_purchase_timestamp"] = pd.to_datetime(
    df["order_purchase_timestamp"], errors="coerce"
)

st.title("E-Commerce Dashboard")
st.caption(
    "Sales Performance, Delivery Performance, and Customer Satisfaction"
)

# Sidebar filters
st.sidebar.header("Filters")

years = sorted(df["order_year"].dropna().unique())
selected_years = st.sidebar.multiselect(
    "Year",
    options=years,
    default=years
)

categories = sorted(
    df["product_category_name_english"].dropna().unique()
)
selected_categories = st.sidebar.multiselect(
    "Product Category",
    options=categories,
    default=[]
)

filtered = df[df["order_year"].isin(selected_years)].copy()

if selected_categories:
    filtered = filtered[
        filtered["product_category_name_english"].isin(selected_categories)
    ]

# KPI
total_revenue = filtered["revenue"].sum()
total_orders = filtered["order_id"].nunique()
avg_review = filtered["review_score"].mean()

delivery_filtered = filtered[
    filtered["delivery_status"].notna()
]
on_time_rate = (
    (delivery_filtered["delivery_status"] == "On Time").mean() * 100
    if len(delivery_filtered) > 0 else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Orders", f"{total_orders:,.0f}")
col3.metric("Average Review", f"{avg_review:.2f} / 5")
col4.metric("On-Time Rate", f"{on_time_rate:.2f}%")

st.divider()

# Sales section
st.header("1. Sales Performance")

monthly_filtered = (
    filtered.groupby("order_month", as_index=False)
    .agg(
        revenue=("revenue", "sum"),
        total_orders=("order_id", "nunique")
    )
    .sort_values("order_month")
)

fig_monthly = px.line(
    monthly_filtered,
    x="order_month",
    y="revenue",
    markers=True,
    title="Monthly Revenue Trend"
)
fig_monthly.update_layout(
    xaxis_title="Month",
    yaxis_title="Revenue"
)
st.plotly_chart(fig_monthly, use_container_width=True)

category_filtered = (
    filtered.groupby("product_category_name_english", as_index=False)
    .agg(
        revenue=("revenue", "sum"),
        total_orders=("order_id", "nunique")
    )
    .sort_values("revenue", ascending=False)
    .head(10)
    .sort_values("revenue")
)

fig_category = px.bar(
    category_filtered,
    x="revenue",
    y="product_category_name_english",
    orientation="h",
    title="Top 10 Product Categories by Revenue"
)
fig_category.update_layout(
    xaxis_title="Revenue (R$)",
    yaxis_title="Product Category"
)
st.plotly_chart(fig_category, use_container_width=True)

st.divider()

# Delivery section
st.header("2. Delivery & Customer Satisfaction")

delivery_filtered = filtered[
    filtered["delivery_status"].notna() &
    filtered["review_score"].notna()
].copy()

delivery_summary = (
    delivery_filtered.groupby("delivery_status", as_index=False)
    .agg(
        avg_review_score=("review_score", "mean"),
        total_orders=("order_id", "nunique")
    )
)

col1, col2 = st.columns(2)

with col1:
    fig_delivery = px.bar(
        delivery_summary,
        x="delivery_status",
        y="avg_review_score",
        title="Average Review Score by Delivery Status",
        text_auto=".2f"
    )
    fig_delivery.update_yaxes(range=[0, 5])
    st.plotly_chart(fig_delivery, use_container_width=True)

with col2:
    fig_box = px.box(
        delivery_filtered,
        x="delivery_status",
        y="review_score",
        title="Review Score Distribution"
    )
    st.plotly_chart(fig_box, use_container_width=True)

st.divider()

st.header("3. Key Findings")

if not monthly_filtered.empty:
    peak = monthly_filtered.loc[
        monthly_filtered["revenue"].idxmax()
    ]
    st.write(
        f"• **Peak monthly revenue:** {peak['order_month']} "
        f"with **${peak['revenue']:,.0f}**."
    )

if not category_filtered.empty:
    top_cat = category_filtered.sort_values(
        "revenue", ascending=False
    ).iloc[0]
    st.write(
        f"• **Top revenue category:** "
        f"**{top_cat['product_category_name_english']}** "
        f"with **${top_cat['revenue']:,.0f}**."
    )

if len(delivery_summary) >= 2:
    scores = delivery_summary.set_index("delivery_status")[
        "avg_review_score"
    ]
    if "On Time" in scores.index and "Late" in scores.index:
        diff = scores["On Time"] - scores["Late"]
        st.write(
            f"• **Review score difference:** On Time orders have "
            f"an average score **{diff:.2f} points** different from Late orders."
        )

st.info(
    "Action Item: prioritize high-revenue product categories and "
    "investigate sellers/areas with frequent delivery delays to "
    "improve customer satisfaction."
)
