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

    st.subheader("Dataset Preview")
    st.dataframe(df)

    st.subheader("🔍 Dataset Exploration")

    st.write("Status Values")
    st.write(df["status"].unique())

    st.write("Policy Types")
    st.write(df["policy_type"].unique())

    st.write("Application Date Sample")
    st.write(df["application_date"].head())

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())
