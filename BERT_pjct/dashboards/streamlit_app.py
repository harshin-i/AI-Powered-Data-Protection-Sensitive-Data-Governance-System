
import streamlit as st
import pandas as pd, os, json

st.set_page_config(page_title="Data Protection Dashboard", layout="wide")
st.title("AI-Powered Data Protection Dashboard")

if not os.path.exists("reports/protected_sample.csv"):
    st.info("Run the pipeline notebook first to produce reports in reports/.")
else:
    protected = pd.read_csv("reports/protected_sample.csv")
    anomalies = pd.read_csv("reports/anomalies_detected.csv")
    with open("reports/compliance_report.json") as f:
        compliance = json.load(f)

    st.header("Protected Sample (preview)")
    st.dataframe(protected.head(100))

    st.header("Sensitivity distribution")
    st.bar_chart(protected['sensitivity'].value_counts())

    st.header("Policy Violations")
    st.write("Total violations:", compliance.get("summary",{}).get("total_violations",0))
    st.json(compliance.get("violations", []))

    st.header("Anomalies")
    st.write("Total anomalies:", int(anomalies['anomaly'].sum()))
    st.dataframe(anomalies.head(100))

    st.markdown("## Download Reports")
    st.markdown("- reports/protected_sample.csv")
    st.markdown("- reports/anomalies_detected.csv")
    st.markdown("- reports/compliance_report.json")
