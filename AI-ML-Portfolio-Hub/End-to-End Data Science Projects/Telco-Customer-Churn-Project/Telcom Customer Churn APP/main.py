import pandas as pd
import pickle
from enum import Enum

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# ==== Enums ====
class YesNo (str, Enum):
    Yes = "Yes"
    No = "No"
    
class InternetServices (str, Enum):
    DSL = "DSL"
    Fiber = "Fiber optic"
    No = "No"
    
class Contracts (str, Enum):
    MontlyToMonth = "Month-to-month"
    OneYear = "One year"
    TwoYear = "Two year"
    
class PaymentMethods (str, Enum):
    ElectronicCheck = "Electronic check"
    MailedCheck = "Mailed check"
    BankTransfer = "Bank transfer (automatic)"
    CreditCard = "Credit card (automatic)"
    
# ==== Input Model ====
class CustomerData(BaseModel):
    SeniorCitizen : int = Field(..., ge=0, le=1,description="0 = not senior, 1 = senior" )
    Partner : YesNo
    Dependents : YesNo
    tenure : int = Field(...,ge=0,description="Months with the company")
    PhoneService : YesNo
    MultipleLines : YesNo
    InternetService : InternetServices
    OnlineSecurity : YesNo
    OnlineBackup : YesNo
    DeviceProtection : YesNo
    TechSupport : YesNo
    StreamingTV : YesNo
    StreamingMovies : YesNo
    Contract : Contracts
    PaperlessBilling : YesNo
    PaymentMethod : PaymentMethods
    MonthlyCharges : float = Field(..., ge= 0, description= "Current months charges")
    TotalCharges : float = Field(..., ge= 0, description= "Current total amount paid by customer")
    
    def to_df (self):
        return pd.DataFrame([self.model_dump()])
    
    
# ==== Output Model ====
class PredictionOut(BaseModel):
    prediction: int
    label: str
    churn_probability: float
    
# ==== load Model ====
with open("XGBOOST_pipline.pkl", "rb") as file:
    model = pickle.load(file)
    
# ==== FastApi App ====
app = FastAPI(
    title= "Telcom Customer Churn Predictor",
    description= "API for predicting churn based on customer data")

# === label CORS ====
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"]   
)

# ==== Health Check ====
@app.get("/health")
def health_check():
    return {"status": "OK"}

# ==== Route Endpoints 
@app.get("/")
def route():
    return {"message : Welcome to Telcom Churn API, visit /docs to test the model."}

# ==== Prediction Endpoints ====
@app.post("/predict",response_model=PredictionOut)
def predict(data : CustomerData):
    input_df = data.to_df()
    prediction = int(model.predict(input_df)[0])
    probability = round(model.predict_proba(input_df)[0][1], 4)
    label = "churn" if prediction == 1 else "Stay"
    
    return {
        "prediction" : prediction,
        "label" : label,
        "churn_probability" : probability
    }

