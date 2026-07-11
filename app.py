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

    ## Dataset
    st.subheader("Dataset Preview")
    st.dataframe(df)

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


    with st.expander("🔍 Dataset Exploration (Developer View)"):

        st.write("Status Values")
        st.write(df["status"].unique())

        st.write("Policy Types")
        st.write(df["policy_type"].unique())

        st.write("Application Date Sample")
        st.write(df["application_date"].head())

    
