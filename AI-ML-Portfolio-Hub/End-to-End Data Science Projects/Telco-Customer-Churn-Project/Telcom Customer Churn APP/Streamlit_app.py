# Name : Mohamed Reda Ramadan Khamis
# Phone Number : 01554725661


import streamlit as st
import pandas as pd
import pickle

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📉",
    layout="centered"
)

# =========================
# Load Model
# =========================
with open("XGBOOST_pipline.pkl", "rb") as file:
    model = pickle.load(file)

# =========================
# Custom CSS
# =========================
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}
h1 {
    text-align: center;
    color: #0d6efd;
}
.stButton>button {
    width: 100%;
    background-color: #0d6efd;
    color: white;
    font-size: 18px;
    border-radius: 10px;
}
.stButton>button:hover {
    background-color: #084298;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# =========================
# Title Section
# =========================
st.title("📉 Customer Churn Prediction")
st.markdown(
    "<p style='text-align:center;color:gray;'>Predict whether a customer is likely to churn based on their service usage</p>",
    unsafe_allow_html=True
)

st.markdown("<div class='card'>", unsafe_allow_html=True)

# =========================
# Helper Function
# =========================
def selectbox_placeholder(label, options):
    return st.selectbox(label, ["Select..."] + options)

# =========================
# Input Layout
# =========================
col1, col2 = st.columns(2)

with col1:
    SeniorCitizen = selectbox_placeholder("Senior Citizen", ["0", "1"])
    Partner = selectbox_placeholder("Partner", ["Yes", "No"])
    Dependents = selectbox_placeholder("Dependents", ["Yes", "No"])
    PhoneService = selectbox_placeholder("Phone Service", ["Yes", "No"])
    MultipleLines = selectbox_placeholder("Multiple Lines", ["Yes", "No"])
    InternetService = selectbox_placeholder("Internet Service", ["DSL", "Fiber optic"])
    OnlineSecurity = selectbox_placeholder("Online Security", ["Yes", "No"])
    OnlineBackup = selectbox_placeholder("Online Backup", ["Yes", "No"])
    DeviceProtection = selectbox_placeholder("Device Protection", ["Yes", "No"])

with col2:
    TechSupport = selectbox_placeholder("Tech Support", ["Yes", "No"])
    StreamingTV = selectbox_placeholder("Streaming TV", ["Yes", "No"])
    StreamingMovies = selectbox_placeholder("Streaming Movies", ["Yes", "No"])
    Contract = selectbox_placeholder("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = selectbox_placeholder("Paperless Billing", ["Yes", "No"])
    PaymentMethod = selectbox_placeholder(
        "Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    )
    tenure = st.text_input("Tenure (Months)")
    MonthlyCharges = st.text_input("Monthly Charges")
    TotalCharges = st.text_input("Total Charges")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("")

# =========================
# Prediction
# =========================
if st.button("🔍 Predict Churn"):
    inputs = {
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "tenure": tenure,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    # Validation
    if "Select..." in inputs.values() or "" in inputs.values():
        st.warning("⚠️ Please complete all fields before prediction.")
    else:
        try:
            df = pd.DataFrame([inputs])
            df["tenure"] = pd.to_numeric(df["tenure"])
            df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"])
            df["TotalCharges"] = pd.to_numeric(df["TotalCharges"])

            prediction = model.predict(df)[0]

            st.markdown("---")

            if prediction == 1:
                st.error("🚨 **High Risk of Churn**\n\nThis customer is likely to leave the service.")
            else:
                st.success("✅ **Low Risk of Churn**\n\nThis customer is likely to stay.")

        except:
            st.error("❌ Please enter valid numeric values.")
