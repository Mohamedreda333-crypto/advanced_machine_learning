import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder ,OrdinalEncoder ,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from imblearn.pipeline import Pipeline as ImbPipeline

from xgboost import XGBClassifier
from sklearn.metrics import classification_report

from imblearn.over_sampling import SMOTE 

import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv("C:/Users/PC/Desktop/machine learning/Data Science Projects/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Drop Unnecessary Columns
df.drop(['customerID','gender'], axis =1, inplace=True)

# Convert TotalCharges columns to nemuric and handle missing values
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors='coerce')
df["TotalCharges"]=df["TotalCharges"].fillna(0)

# Handle 'No internet service' and 'No phone service'
df.replace(['No internet service','No phone service'],'No',inplace=True)

# Encode Target Column using Label Encoding or using Binary mapping
df["Churn"] = df["Churn"].map({"Yes" : 1, "No": 0})

# Split Data and Target
x = df.drop("Churn", axis=1)
y = df["Churn"]

x_train, x_test, y_train, y_test = train_test_split(x,y,stratify=y,test_size=0.2,random_state=42)



numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
binary_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'SeniorCitizen']
ordinal_cols = ['Contract']
categorical_cols = ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
    'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaymentMethod' ]

# Numeric Pipeline
numeric_pipeline = Pipeline(steps=[
    ("imputer",SimpleImputer(strategy="median")),
    ("scalar",StandardScaler())
])

# Binary Pipline
binary_pipeline = Pipeline(steps=[
     ("imputer",SimpleImputer(strategy="most_frequent")),
    ('onehot', OneHotEncoder(drop='if_binary', handle_unknown='ignore'))
])

# Ordinal Pipeline (Contract)
ordinal_pipeline = Pipeline(steps = [
    ("imputer",SimpleImputer(strategy="most_frequent")),
    ('ordinal', OrdinalEncoder(categories=[['Month-to-month', 'One year', 'Two year']]))
])

# Categorical Pipeline (Multi-category)
categorical_pipeline = Pipeline([
    ("imputer",SimpleImputer(strategy="most_frequent")),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_pipeline, numeric_cols),
        ('bin', binary_pipeline, binary_cols),
        ('ord', ordinal_pipeline, ordinal_cols),
        ('cat', categorical_pipeline, categorical_cols)
    ],
    remainder='drop'
)

# Training Pipeline
training_pipeline = ImbPipeline(steps=[
    ('preprocessing', preprocessor),  # Encoding + Scaling
    ('smote', SMOTE(random_state=42)), # Handle imbalance
    ('model', XGBClassifier(
        colsample_bytree=1.0,
        learning_rate=0.03,
        max_depth=4,
        n_estimators=200,
        subsample=0.8,
        eval_metric='mlogloss',
        use_label_encoder=False
    ))
])

# Fit Pipline on Data
training_pipeline.fit(x_train,y_train)

# Evaluation
y_pred = training_pipeline.predict(x_test)
print("\n classification_report")
print(classification_report(y_test,y_pred))

# Save Model
with open ("XGBOOST_pipline.pkl","wb") as f:
    pickle.dump(training_pipeline,f)
    
print("\n Model Saved Successfully to XGBOOST_pipline.pkl ")