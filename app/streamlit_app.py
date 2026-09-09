import streamlit as st
import pandas as pd

st.markdown("""
<style>

.kpi-card {
    background: rgba(24, 35, 52, 0.85);
    border: 1px solid rgba(120, 150, 190, 0.25);
    border-radius: 14px;
    padding: 22px;
    min-height: 145px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.15);
}

.compact-kpi {
    min-hight: 180px !important;
}

.kpi-title {
    font-size: 17px;
    font-weight: 600;
    margin-bottom: 12px;
    color: #f1f5f9;
}

.kpi-value {
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 8px;
    color: #ffffff;
}

.kpi-description {
    font-size: 14px;
    color: #c5ccd8;
    line-height: 1.4;
}

.section-title {
    font-size: 30px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 20px;
}

.summary-card {
    background: rgba(23, 35, 52, 0.85);
    border: 1px solid rgba(100, 150, 200, 0.30);
    border-radius: 14px;
    padding: 24px 28px;
    margin-top: 0px;
    min-height: 150px;
}

.summary-title {
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 20px;
    color: #ffffff;
}

.summary-metrics {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;
}

.summary-metric {
    flex: 1;
    padding: 0 10px;
}

.summary-label {
    font-size: 17px;
    font-weight: 600;
    margin-bottom: 8px;
    color: #f1f5f9;
}

.summary-value {
    font-size: 28px;
    font-weight: 700;
    color: #ffffff;
}

.summary-divider {
    width: 1px;
    height: 55px;
    background: rgba(180, 200, 220, 0.25);
}

.engagement-card {
    background: rgba(23, 35, 52, 0.85);
    border: 1px solid rgba(150, 120, 220, 0.45);
    border-radius: 14px;
    padding: 24px 28px;
    margin-top: 10px;
    margin-bottom: 25px;
}

.engagement-title {
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 6px;
    color: #ffffff;
}

.engagement-subtitle {
    font-size: 15px;
    color: #c5ccd8;
    margin-bottom: 24px;
}

.engagement-metrics {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;
}

.engagement-metric {
    flex: 1;
    padding: 0 10px;
}

.engagement-label {
    font-size: 17px;
    font-weight: 600;
    margin-bottom: 8px;
    color: #f1f5f9;
}

.engagement-value {
    font-size: 32px;
    font-weight: 700;
    color: #ffffff;
}

.engagement-description {
    font-size: 14px;
    color: #c5ccd8;
    margin-top: 4px;
}

.engagement-divider {
    width: 1px;
    height: 70px;
    background: rgba(180, 200, 220, 0.25);
}

.engagement-drop {
    background: rgba(90, 70, 150, 0.25);
    border: 1px solid rgba(160, 130, 230, 0.30);
    border-radius: 12px;
    padding: 18px 22px;
}

.engagement-drop-label {
    font-size: 17px;
    font-weight: 600;
    margin-bottom: 5px;
    color: #f1f5f9;
}

.engagement-drop-value {
    font-size: 32px;
    font-weight: 700;
    color: #b58cff;
}

.engagement-drop-description {
    font-size: 14px;
    color: #c5ccd8;
    line-height: 1.4;
}
</style>
""", unsafe_allow_html=True)



# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="European Bank Churn Analytics",
    page_icon="🏦",
    layout="wide"
)

# Load dataset
df = pd.read_csv("data/raw/European_Bank.csv")

# Sidebar filters
st.sidebar.header("Segment Filters")

selected_geography = st.sidebar.selectbox(
    "Geography",
    ["All", "France", "Germany", "Spain"]
)

# Create age segments
df["AgeSegment"] = pd.cut(
    df["Age"],
    bins=[0, 29, 45, 60, float("inf")],
    labels=["Under 30", "30-45", "46-60", "60+"]
)

selected_age = st.sidebar.selectbox(
    "Age Segment",
    ["All", "Under 30", "30-45", "46-60", "60+"]
)

# Create credit score segments
df["CreditScoreSegment"] = pd.cut(
    df["CreditScore"],
    bins=[-float("inf"), 579, 669, float("inf")],
    labels=["Low", "Medium", "High"]
)

selected_credit_score = st.sidebar.selectbox(
    "Credit Score",
    ["All", "Low", "Medium", "High"]
)

# Create tenure segments
df["TenureSegment"] = pd.cut(
    df["Tenure"],
    bins=[-1, 3, 7, 10],
    labels=["New", "Mid-term", "Long-term"]
)

selected_tenure = st.sidebar.selectbox(
    "Tenure",
    ["All", "New", "Mid-term", "Long-term"]
)

# Create balance segments
df["BalanceSegment"] = pd.cut(
    df["Balance"],
    bins=[-0.01, 0, 99999.99, float("inf")],
    labels=["Zero Balance", "Low Balance", "High Balance"]
)

selected_balance = st.sidebar.selectbox(
    "Balance",
    ["All", "Zero Balance", "Low Balance", "High Balance"]
)

# ---------------------------------------------------------
# Apply filters
# ---------------------------------------------------------
filtered_df = df.copy()

if selected_geography != "All":
    filtered_df = filtered_df[
        filtered_df["Geography"] == selected_geography
    ]

if selected_age != "All":
    filtered_df = filtered_df[
        filtered_df["AgeSegment"] == selected_age
    ]

if selected_credit_score != "All":
    filtered_df = filtered_df[
        filtered_df["CreditScoreSegment"] == selected_credit_score
    ]

if selected_tenure != "All":
    filtered_df = filtered_df[
        filtered_df["TenureSegment"] == selected_tenure
    ]

if selected_balance != "All":
    filtered_df = filtered_df[
        filtered_df["BalanceSegment"] == selected_balance
    ]

# Page title
st.title("European Bank Customer Churn Analytics")

st.write(
    "Interactive analysis of customer segmentation and churn patterns."
)

# Overall bank churn rate
overall_total_customers = len(df)
overall_churned_customers = df["Exited"].sum()
overall_churn_rate = (
    overall_churned_customers / overall_total_customers
) * 100

# Geographic Risk Index
if selected_geography == "All":
    geographic_risk_index = 100
else:
    geography_churn_rate = (
        df[df["Geography"] == selected_geography]["Exited"].mean()
    ) * 100

    geographic_risk_index = (
        geography_churn_rate / overall_churn_rate
    ) * 100

# Engagement Drop Indicator
inactive_customers = filtered_df[filtered_df["IsActiveMember"] == 0]
active_customers = filtered_df[filtered_df["IsActiveMember"] == 1]

if len(inactive_customers) > 0:
    inactive_churn_rate = inactive_customers["Exited"].mean() * 100
else:
    inactive_churn_rate = 0

if len(active_customers) > 0:
    active_churn_rate = active_customers["Exited"].mean() * 100
else:
    active_churn_rate = 0

engagement_drop_indicator = (
    inactive_churn_rate - active_churn_rate
)

# Filtered segment churn rate
segment_total_customers = len(filtered_df)
segment_churned_customers = filtered_df["Exited"].sum()
total_customers = segment_total_customers
churned_customers = segment_churned_customers
retained_customers = total_customers - churned_customers

if segment_total_customers > 0:
    segment_churn_rate = (
        segment_churned_customers / segment_total_customers
    ) * 100
else:
    segment_churn_rate = 0

# High-value churn ratio within selected segment
high_balance_segment = filtered_df[
    filtered_df["BalanceSegment"] == "High Balance"
]

if len(high_balance_segment) > 0:
    high_value_churn_ratio = (
        high_balance_segment["Exited"].sum()
        / len(high_balance_segment)
    ) * 100
else:
    high_value_churn_ratio = 0

# ---------------------------------------------------------
# KPI section
# ---------------------------------------------------------

st.markdown("## 📊 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">👥 Overall Churn Rate</div>
            <div class="kpi-value">{overall_churn_rate:.2f}%</div>
            <div class="kpi-description">
                Share of all customers who churned
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">📈 Segment Churn Rate</div>
            <div class="kpi-value">{segment_churn_rate:.2f}%</div>
            <div class="kpi-description">
                Churn rate for selected segment
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="kpi-card compact-kpi">
            <div class="kpi-title">💎 High-Value Churn Ratio</div>
            <div class="kpi-value">{high_value_churn_ratio:.2f}%</div>
            <div class="kpi-description">
                Churn rate among high-balance customers
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

# SECOND KPI ROW

geo_col, summary_col = st.columns([1, 2])

# Geographic Risk Index
with geo_col:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">📍 Geographic Risk Index</div>
            <div class="kpi-value">{geographic_risk_index:.2f}</div>
            <div class="kpi-description">
                Relative churn risk (Germany = 100)
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Customer Summary
with summary_col:
    st.markdown(
        f"""
<div class="summary-card">
<div class="summary-title">
        👥 Customer Summary
    </div>

<div class="summary-metrics">
        <div class="summary-metric">
            <div class="summary-label">Total Customers</div>
            <div class="summary-value">{total_customers:,}</div>
        </div>

<div class="summary-divider"></div>

<div class="summary-metric">
            <div class="summary-label">Churned Customers</div>
            <div class="summary-value churned">{churned_customers:,}</div>
        </div>

<div class="summary-divider"></div>

<div class="summary-metric">
            <div class="summary-label">Retained Customers</div>
            <div class="summary-value retained">{retained_customers:,}</div>
        </div>
    </div>
</div>
        """,
        unsafe_allow_html=True
    )

# Engagement and churn comparison
st.markdown(
    f"""
<div class="engagement-card">

<div class="engagement-title">
        👥 Engagement & Churn
    </div>

<div class="engagement-subtitle">
        Inactivity vs churn analysis for the selected segment.
    </div>

<div class="engagement-metrics">

<div class="engagement-metric">
<div class="engagement-label">
                Inactive Customers
        </div>

<div class="engagement-value">
                {inactive_churn_rate:.2f}%
            </div>

<div class="engagement-description">
                churn rate
            </div>
        </div>

<div class="engagement-divider"></div>

<div class="engagement-metric">
<div class="engagement-label">
                Active Customers
            </div>

<div class="engagement-value">
                {active_churn_rate:.2f}%
            </div>

 <div class="engagement-description">
                churn rate
            </div>
        </div>

<div class="engagement-divider"></div>

<div class="engagement-metric engagement-drop">
<div class="engagement-drop-label">
                Engagement Drop
            </div>

<div class="engagement-drop-value">
                {engagement_drop_indicator:.2f} pp
            </div>

<div class="engagement-drop-description">
                Inactive customers have a higher churn rate
                than active customers within the selected segment.
            </div>
        </div>

</div>

</div>
    """,
    unsafe_allow_html=True
)


# GEOGRAPHY-WISE CHURN ANALYSIS

st.markdown("---")
st.header("Churn Analysis")

st.write(
    "Explore churn patterns across geography, age, and customer tenure."
)

st.subheader("Geography-wise Churn Rate")

geo_churn = (
    filtered_df.groupby("Geography")["Exited"]
    .mean()
    .mul(100)
    .reset_index(name="Churn Rate")
)

st.bar_chart(
    geo_churn.set_index("Geography")["Churn Rate"]
)

# AGE-WISE CHURN ANALYSIS

st.subheader("Age-wise Churn Rate")

age_churn = (
    filtered_df.groupby("AgeSegment")["Exited"]
    .mean()
    .mul(100)
    .reset_index(name="Churn Rate")
)

st.bar_chart(
    age_churn.set_index("AgeSegment")["Churn Rate"]
)

# TENURE-WISE CHURN ANALYSIS

st.subheader("Tenure-wise Churn Rate")

tenure_churn = (
    filtered_df.groupby("TenureSegment")["Exited"]
    .mean()
    .mul(100)
    .reset_index(name="Churn Rate")
)

st.bar_chart(
    tenure_churn.set_index("TenureSegment")["Churn Rate"]
)

# HIGH-VALUE CUSTOMER CHURN EXPLORER
st.markdown("---")
st.header("High-Value Customer Risk")

st.write(
    "Explore churn among high-balance customers and the balance exposure associated with churn."
)

st.subheader("High-Value Customer Churn Explorer")

high_value_df = filtered_df[
    filtered_df["BalanceSegment"] == "High Balance"
]

high_value_churners = high_value_df[
    high_value_df["Exited"] == 1
]

hv_col1, hv_col2, hv_col3, hv_col4 = st.columns(4)

with hv_col1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">💰 High-Balance Customers</div>
            <div class="kpi-value">{len(high_value_df):,}</div>
            <div class="kpi-description">
                Customers with high balance
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with hv_col2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">⚠️ High-Balance Churners</div>
            <div class="kpi-value">{len(high_value_churners):,}</div>
            <div class="kpi-description">
                High-balance customers who churned
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with hv_col3:
    high_value_churn_rate = (
        len(high_value_churners) / len(high_value_df) * 100
        if len(high_value_df) > 0
        else 0
    )

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">📉 Churn Rate</div>
            <div class="kpi-value">{high_value_churn_rate:.2f}%</div>
            <div class="kpi-description">
                Churn rate among high-balance customers
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with hv_col4:
    balance_exposure = high_value_churners["Balance"].sum()

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">💼 Balance Exposure</div>
            <div class="kpi-value">{balance_exposure / 1_000_000:.2f}M</div>
            <div class="kpi-description">
                Balance exposure associated with high-balance churners
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# SALARY VS BALANCE ANALYSIS
st.markdown("<div style='height: 35px;'></div>", unsafe_allow_html=True)
st.subheader("Salary vs Balance: High-Balance Churners")

if len(high_value_churners) > 0:

    salary_balance = high_value_churners[
        ["EstimatedSalary", "Balance"]
    ].copy()

    correlation = salary_balance[
        "EstimatedSalary"
    ].corr(salary_balance["Balance"])

    st.scatter_chart(
        salary_balance,
        x="EstimatedSalary",
        y="Balance"
    )

    st.write(
        f"**Pearson correlation:** {correlation:.4f}"
    )

    st.caption(
        "The correlation measures the linear association between "
        "estimated salary and balance among high-balance customers who churned."
    )

else:
    st.info(
        "No high-balance churners are available for the selected filters."
    )

# Balance Exposure Associated with Churn

st.subheader("Balance Exposure Associated with Churn")

# All churned customers within the current filter selection
churned_customers = filtered_df[filtered_df["Exited"] == 1]

# High-balance churners within the current filter selection
high_balance_churners = churned_customers[
    churned_customers["BalanceSegment"] == "High Balance"
]

# Calculate balance exposure
total_churned_balance = churned_customers["Balance"].sum()
high_balance_churned_balance = high_balance_churners["Balance"].sum()

# Remaining churned balance exposure
other_churned_balance = (
    total_churned_balance - high_balance_churned_balance
)

# Share of churned balance exposure from high-balance churners
if total_churned_balance > 0:
    high_balance_exposure_share = (
        high_balance_churned_balance / total_churned_balance
    ) * 100
else:
    high_balance_exposure_share = 0


# Display balance exposure metrics
exposure_col1, exposure_col2, exposure_col3 = st.columns(3)

with exposure_col1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">💰 Total Churned Balance</div>
            <div class="kpi-value">{total_churned_balance:,.2f}</div>
            <div class="kpi-description">
                Total balance associated with churned customers
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with exposure_col2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">🏦 High-Balance Churned Balance</div>
            <div class="kpi-value">{high_balance_churned_balance:,.2f}</div>
            <div class="kpi-description">
                Balance associated with high-balance churners
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with exposure_col3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">📊 High-Balance Exposure Share</div>
            <div class="kpi-value">{high_balance_exposure_share:.2f}%</div>
            <div class="kpi-description">
                Share of churned balance exposure from high-balance churners
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.caption(
    "Balance exposure represents the total customer balance associated "
    "with churned customers. It is used as a proxy for potential financial risk, "
    "not as a measure of actual lost revenue."
)