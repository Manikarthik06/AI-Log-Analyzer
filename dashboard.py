import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from rag_analyzer import ask_rag
import os
from pdf_generator import create_incident_pdf
print("=" * 50)
print("Current Working Directory:")
print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("Script Location:")
print(BASE_DIR)

DB_PATH = os.path.join(BASE_DIR, "chroma_db")
print("Database Path:")
print(DB_PATH)
print("=" * 50)
st.set_page_config(
    page_title="AI Log Analyzer",
    layout="wide"
)

st.title("🔍 AI Log Analyzer Dashboard")

# Upload log file
uploaded_file = st.file_uploader(
    "Upload Log File",
    type=["log", "txt"]
)

if uploaded_file is not None:

    logs = uploaded_file.read().decode("utf-8").splitlines()

    st.success(f"Loaded {len(logs)} log entries")

    # Create simple dataframe
    df = pd.DataFrame({"Log Message": logs})

    st.subheader("Raw Logs")
    st.dataframe(df)

    # --------------------
    # Statistics
    # --------------------

    total_logs = len(df)

    failed_logins = df["Log Message"].str.contains(
        "failed|failure|invalid",
        case=False,
        na=False
    ).sum()

    successful_logins = df["Log Message"].str.contains(
        "accepted|success",
        case=False,
        na=False
    ).sum()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Logs", total_logs)
    col2.metric("Failed Logins", failed_logins)
    col3.metric("Successful Logins", successful_logins)

    # --------------------
    # Severity
    # --------------------

    suspicious_keywords = [
        "failed",
        "failure",
        "invalid",
        "denied",
        "attack",
        "scan",
        "timeout"
    ]

    suspicious_count = df["Log Message"].str.contains(
        "|".join(suspicious_keywords),
        case=False,
        na=False
    ).sum()

    if suspicious_count < 10:
        severity = "LOW"
    elif suspicious_count < 50:
        severity = "MEDIUM"
    else:
        severity = "HIGH"

    st.subheader("Overall Severity")

    st.write(f"### {severity}")

    # --------------------
    # Chart
    # --------------------

    st.subheader("Log Summary")

    chart_df = pd.DataFrame({
        "Category": [
            "Failed Logins",
            "Successful Logins",
            "Suspicious Events"
        ],
        "Count": [
            failed_logins,
            successful_logins,
            suspicious_count
        ]
    })

    fig, ax = plt.subplots()

    ax.bar(
        chart_df["Category"],
        chart_df["Count"]
    )

    st.pyplot(fig)

    # --------------------
    # AI Query Section
    # --------------------

    st.subheader("Ask AI About Logs")

    user_query = st.text_input(
        "Enter your question"
    )

    if st.button("Analyze"):

        response = ask_rag(user_query)

        st.subheader("Cybersecurity Incident Report")

        st.write(response)

        pdf = create_incident_pdf(response)

        st.download_button(
            label="📄 Download Incident Report",
            data=pdf,
            file_name="Cybersecurity_Incident_Report.pdf",
            mime="application/pdf"
        )