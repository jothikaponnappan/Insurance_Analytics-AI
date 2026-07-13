import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Insurance Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Insurance Policy Analytics")

uploaded_file = st.file_uploader(
    "Upload Insurance CSV",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Columns")
    st.dataframe(pd.DataFrame({
    "Column Name": df.columns
    }))

    st.success("✅ Dataset Loaded Successfully!")
    st.subheader("📊 Dashboard KPIs")
    total_policies = len(df)

    issued_policies = df[df["status"] == "Issued"].shape[0]

    failed_policies = df[df["status"] == "Failed"].shape[0]
    pending_policies = df[df["status"] == "Pending"].shape[0]

    total_premium = df["premium_amount"].sum()

    avg_processing_time = df["processing_time_hours"].mean()
        
        
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Policies", f"{total_policies:,}")
    col2.metric("Issued Policies", f"{issued_policies:,}")
    col3.metric("Failed Policies", f"{failed_policies:,}")

    col4, col5, col6 = st.columns(3)

    col4.metric("Pending Policies", f"{pending_policies:,}")

    col5.metric("Total Premium", f"₹ {total_premium:,.2f}")

    col6.metric("Avg Processing Time", f"{avg_processing_time:.2f} hrs")

    # Policy status distribution
    st.subheader("📊 Policy Status Distribution")

    status_count = (
        df["status"]
        .value_counts()
        .reset_index()
    )

    status_count.columns = ["Status", "Count"]

    fig = px.bar(
        status_count,
        x="Status",
        y="Count",
        title="Policies by Status",
        text="Count"
    )

    st.plotly_chart(fig, use_container_width=True)

    #Policy Type Distribution
    st.subheader("📊 Policy Type Distribution")
    policy_count = df["policy_type"].value_counts().reset_index()
    policy_count.columns=["Policy Type", "Count"]
    fig_1 = px.bar(
        policy_count,
        x="Policy Type",
        y="Count",
        title="Policies by Type",
        text="Count"
    )

    st.plotly_chart(fig_1, use_container_width=True)

    st.subheader("📊 Policy Premium Distribution")
    premium_by_policy = (
    df
        .groupby("policy_type")
        ["premium_amount"]
        .sum()
        .reset_index()
)
    premium_by_policy.columns=["Policy Type", "Premium"]
    premium_by_policy=premium_by_policy.sort_values(by="Premium",
    ascending=False)
    fig_2= px.bar(
        premium_by_policy,
        x="Policy Type",
        y="Premium",
        title="premium by policy",
        text="Premium"
    )

    st.plotly_chart(fig_2, use_container_width=True)
    
    st.subheader("📊 Top Failure Reasons")
    failure_df=df[df['status']=='Failed']
    failure_reason=failure_df['failure_reason'].value_counts().reset_index()
    failure_reason.columns=["Failure Reason", "Count"]
    failure_reason=failure_reason.sort_values(by="Count",
    ascending=False)
    fig_3= px.bar(
        failure_reason,
        x="Failure Reason",
        y="Count",
        title=" Top Failure Reasons",
        text="Count"
    )
    st.plotly_chart(fig_3, use_container_width=True)

    st.subheader("📊 Monthly Premium Trend")
    df["application_date"] = pd.to_datetime(df["application_date"])

    monthly_premium = (
        df.groupby(df["application_date"].dt.to_period("M"))["premium_amount"]
        .sum()
        .reset_index()
    )

    monthly_premium["application_date"] = monthly_premium["application_date"].astype(str)

    fig_month = px.line(
        monthly_premium,
        x="application_date",
        y="premium_amount",
        markers=True,
        title="Monthly Premium Trend"
    )

    st.plotly_chart(fig_month, use_container_width=True)

    st.subheader("🌍 Premium by Region")
    region_df = (
        df.groupby("region")["premium_amount"]
        .sum()
        .reset_index()
    )

    fig_region = px.bar(
        region_df,
        x="region",
        y="premium_amount",
        text="premium_amount",
        title="Premium by Region"
    )

    st.plotly_chart(fig_region, use_container_width=True)

    st.subheader("⏱ Average Processing Time")
    process_df = (
        df.groupby("policy_type")["processing_time_hours"]
        .mean()
        .reset_index()
    )

    fig_process = px.bar(
        process_df,
        x="policy_type",
        y="processing_time_hours",
        text_auto=".2f",
        title="Average Processing Hours by Policy Type"
    )

    st.plotly_chart(fig_process, use_container_width=True)

     ## Dataset
    st.subheader("Dataset Preview")
    st.dataframe(df)

    with st.expander("🔍 Dataset Exploration (Developer View)"):

        st.write("Status Values")
        st.write(df["status"].unique())

        st.write("Policy Types")
        st.write(df["policy_type"].unique())

        st.write("Application Date Sample")
        st.write(df["application_date"].head())

    
