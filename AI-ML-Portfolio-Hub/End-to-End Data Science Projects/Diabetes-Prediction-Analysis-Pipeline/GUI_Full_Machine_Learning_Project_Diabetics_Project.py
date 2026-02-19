import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import pandas as pd

# ===================== MODEL PATHS =====================
MODEL_PATHS = {
    "Linear Regression": "C:/Users/PC/Desktop/machine learning/linear_regression_pipeline.pkl",
    "Logistic Regression": "logistic_regression_pipeline.pkl",
    "SVM": "svm_tuned_model.pkl",
    "Decision Tree": "decision_tree_tuned.pkl",
    "Random Forest": "random_forest_tuned.pkl",
    "XGBoost": "xgboost_tuned.pkl"
}

# Load encoders
try:
    encoders = joblib.load("label_encoders.pkl")
except:
    encoders = None

# ===================== GUI =====================

root = tk.Tk()
root.title("Diabetes Prediction System")
root.geometry("1300x900")
root.configure(bg="#FFE680")

# ===================== TOP RIGHT EXIT BUTTON =====================
def exit_app():
    root.destroy()

exit_top_btn = tk.Button(root, text="Exit",
                         font=("Arial", 14, "bold"),
                         bg="#8B0000", fg="white",
                         width=10, command=exit_app)
exit_top_btn.place(x=1180, y=10)

# ===================== TITLE =====================
title_label = tk.Label(root, text="Diabetes Prediction System",
                       font=("Arial", 32, "bold"),
                       bg="#FFE680")
title_label.pack(pady=10)

FEATURES = [
    "gender", "age", "hypertension", "heart_disease",
    "smoking_history", "bmi", "HbA1c_level", "blood_glucose_level"
]

# ===================== LAYOUT FRAMES =====================

main_frame = tk.Frame(root, bg="#FFE680")
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

left_frame = tk.Frame(main_frame, bg="#FFE680")
left_frame.pack(side="left", fill="y", padx=10)

right_frame = tk.Frame(main_frame, bg="#FFE680")
right_frame.pack(side="right", fill="both", expand=True, padx=20)

bottom_frame = tk.Frame(root, bg="#FFE680")
bottom_frame.pack(fill="both", padx=20, pady=10)

# ===================== MODEL SELECTION =====================

top_frame = tk.Frame(left_frame, bg="#FFE680")
top_frame.pack(pady=10)

tk.Label(top_frame, text="Model Type:", bg="#FFE680",
         font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5)

model_type_var = tk.StringVar()
model_type_menu = ttk.Combobox(top_frame, width=18, textvariable=model_type_var,
                               values=["Statistical", "Non-Statistical"])
model_type_menu.grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Select Model:", bg="#FFE680",
         font=("Arial", 12, "bold")).grid(row=0, column=2, padx=5)

model_var = tk.StringVar()
model_menu = ttk.Combobox(top_frame, width=18, textvariable=model_var)
model_menu.grid(row=0, column=3, padx=5)

STATISTICAL_MODELS = ["Linear Regression", "Logistic Regression", "SVM"]
NON_STATISTICAL_MODELS = ["Decision Tree", "Random Forest", "XGBoost"]

def update_models(event=None):
    if model_type_var.get() == "Statistical":
        model_menu["values"] = STATISTICAL_MODELS
    else:
        model_menu["values"] = NON_STATISTICAL_MODELS

model_type_menu.bind("<<ComboboxSelected>>", update_models)

# ===================== INPUT FIELDS =====================

inputs_frame = tk.Frame(left_frame, bg="#FFE680")
inputs_frame.pack(pady=10)

entries = {}
gender_options = ["Male", "Female"]
smoke_options = ["never", "former", "ever", "current", "not current", "No Info"]

for i, feature in enumerate(FEATURES):
    tk.Label(inputs_frame, text=feature + ":",
             font=("Arial", 12, "bold"),
             bg="#FFE680").grid(row=i, column=0, pady=5, sticky="w")

    if feature == "gender":
        cb = ttk.Combobox(inputs_frame, values=gender_options, width=22)
        cb.grid(row=i, column=1, padx=10)
        entries[feature] = cb

    elif feature == "smoking_history":
        cb = ttk.Combobox(inputs_frame, values=smoke_options, width=22)
        cb.grid(row=i, column=1, padx=10)
        entries[feature] = cb

    elif feature in ["hypertension", "heart_disease"]:
        cb = ttk.Combobox(inputs_frame, values=["0", "1"], width=22)
        cb.grid(row=i, column=1, padx=10)
        entries[feature] = cb
    else:
        ent = tk.Entry(inputs_frame, width=25)
        ent.grid(row=i, column=1, padx=10)
        entries[feature] = ent

# ===================== MODEL INFORMATION =====================

info_label = tk.Label(right_frame, text="Model Information",
                      font=("Arial", 20, "bold"),
                      bg="#FFE680")
info_label.pack(pady=10)

info_text = tk.Text(right_frame, width=60, height=25,
                    font=("Arial", 12))
info_text.pack(pady=10, fill="both", expand=True)

MODEL_INFO = {

    "Linear Regression":
        """
Linear Regression — Statistical Model

• Type: Statistical model  
• Task: Predict continuous numeric values  
• Preprocessing: One-Hot Encoding + StandardScaler  
• Algorithm: Fits a linear line by minimizing error (least squares)  
• Strengths: Interpretable, fast, simple  
• Weaknesses: Cannot capture non-linear patterns  
        """,

    "Logistic Regression":
        """
Logistic Regression — Statistical Model

• Type: Statistical binary/multi-class classifier  
• Task: Predict probability of a class  
• Preprocessing: One-Hot Encoding + StandardScaler  
• Algorithm: Logistic function with maximum likelihood  
• Strengths: Stable, interpretable  
• Weaknesses: Not good with complex non-linear boundaries  
        """,

    "SVM":
        """
Support Vector Machine — Statistical Model

• Type: Statistical ML model  
• Task: Classification or Regression  
• Preprocessing: One-Hot Encoding + StandardScaler  
• Algorithm: Maximizes the margin between classes  
• Strengths: Performs well with small/medium datasets  
• Weaknesses: Slow with large datasets  
        """,

    "Decision Tree":
        """
Decision Tree — Non-Statistical Model

• Type: Rule-based machine learning model  
• Preprocessing: Label Encoding + StandardScaler  
• Task: Classification or Regression  
• Strengths: Fast, interpretable, handles non-linearity  
• Weaknesses: Easily overfits  
        """,

    "Random Forest":
        """
Random Forest — Non-Statistical Model

• Type: Ensemble of multiple decision trees  
• Preprocessing: Label Encoding + StandardScaler  
• Strengths: Stable, high accuracy, handles noise  
• Weaknesses: Harder to interpret  
        """,

    "XGBoost":
        """
XGBoost — Non-Statistical Model

• Type: Gradient boosting ensemble  
• Preprocessing: Label Encoding + StandardScaler  
• Strengths: Very powerful for structured data, high accuracy  
• Weaknesses: Complex, needs tuning  
        """,
}
def show_info(event=None):
    info_text.delete("1.0", tk.END)
    mdl = model_var.get()
    if mdl in MODEL_INFO:
        info_text.insert(tk.END, MODEL_INFO[mdl])

model_menu.bind("<<ComboboxSelected>>", show_info)

# ===================== PREDICT FUNCTION =====================

def predict():
    model_name = model_var.get()
    if model_name == "":
        messagebox.showerror("Error", "Please select a model!")
        return

    try:
        model = joblib.load(MODEL_PATHS[model_name])
    except:
        messagebox.showerror("Error", f"Model file missing: {MODEL_PATHS[model_name]}")
        return

    input_data = []

    for feature in FEATURES:
        val = entries[feature].get()
        if val == "":
            messagebox.showerror("Error", f"Missing: {feature}")
            return

        if encoders and feature in encoders:
            le = encoders[feature]
            if val in le.classes_:
                val = le.transform([val])[0]
            else:
                val = -1
        else:
            try:
                val = float(val)
            except:
                pass

        input_data.append(val)

    pred = model.predict([input_data])[0]

    result_entry.delete(0, tk.END)
    result_entry.insert(0, str(pred))

# ===================== RESET FUNCTION =====================

def reset_fields():
    for feature in FEATURES:
        try:
            entries[feature].set("")
        except:
            entries[feature].delete(0, tk.END)

    result_entry.delete(0, tk.END)
    info_text.delete("1.0", tk.END)
    model_var.set("")
    model_type_var.set("")

# ===================== BUTTON ANIMATIONS =====================

def on_enter(e):
    e.widget["background"] = "#FF5733"

def on_leave(e):
    e.widget["background"] = "#CC3300"

# ===================== BUTTONS + RESULT BOX SIDE BY SIDE =====================

action_frame = tk.Frame(bottom_frame, bg="#FFE680")
action_frame.pack(pady=20)

predict_btn = tk.Button(action_frame, text="Predict",
                        font=("Arial", 20, "bold"),
                        bg="#CC3300", fg="white",
                        width=15, command=predict)
predict_btn.grid(row=0, column=0, padx=20)

predict_btn.bind("<Enter>", on_enter)
predict_btn.bind("<Leave>", on_leave)

result_entry = tk.Entry(action_frame,
                        font=("Arial", 20, "bold"),
                        width=15, justify="center")
result_entry.grid(row=0, column=1, padx=20)

reset_btn = tk.Button(left_frame, text="Reset",
                      font=("Arial", 16, "bold"),
                      bg="#0066CC", fg="white",
                      width=15, command=reset_fields)
reset_btn.pack(pady=20)



root.mainloop()
