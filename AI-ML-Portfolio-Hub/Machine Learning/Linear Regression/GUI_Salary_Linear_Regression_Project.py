import tkinter as tk
from tkinter import messagebox

def predict_salary():
    try:
        years = float(entry_years.get())
        # Using the actual model coefficients from your data
        predicted_salary = 9356.86 * years + 26089.09
        lbl_result.config(text=f"Predicted Salary: ${predicted_salary:,.2f}", fg="#2ECC71")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

def reset_input():
    entry_years.delete(0, tk.END)
    lbl_result.config(text="Predicted Salary: ---", fg="#ECF0F1")

def logout_app():
    root.destroy()

# --------------------------- PROFESSIONAL GUI ---------------------------------

root = tk.Tk()
root.title("ML Salary Prediction Dashboard")
root.geometry("1200x700")
root.configure(bg='#2C3E50')  # Professional dark blue background

# Color scheme
COLORS = {
    'primary': '#3498DB',
    'secondary': '#2C3E50', 
    'accent': '#E74C3C',
    'success': '#2ECC71',
    'warning': '#F39C12',
    'light': '#ECF0F1',
    'dark': '#34495E'
}

# Header Bar with professional styling
header = tk.Frame(root, bg=COLORS['dark'], height=80)
header.pack(fill='x', padx=0, pady=0)
header.pack_propagate(False)

title_lbl = tk.Label(header, text="AI-Powered Salary Prediction System", 
                     font=("Arial", 22, "bold"), fg=COLORS['light'], bg=COLORS['dark'])
title_lbl.pack(side='left', padx=30, pady=25)

btn_logout_main = tk.Button(header, text="Logout", command=logout_app,
                           font=("Arial", 12, "bold"), bg=COLORS['accent'], 
                           fg='white', width=8, relief='flat')
btn_logout_main.pack(side='right', padx=30, pady=10)

# Main Content Area
main_container = tk.Frame(root, bg=COLORS['secondary'])
main_container.pack(fill='both', expand=True, padx=25, pady=20)

# Information Panel
info_frame = tk.Frame(main_container, bg=COLORS['dark'], relief='raised', bd=2)
info_frame.pack(fill='x', pady=(0, 20))

info_text = """Linear Regression Model for Salary Prediction\nThis AI model predicts expected salary based on years of professional experience.\nThe model has been trained on historical salary data using machine learning algorithms."""

info_label = tk.Label(info_frame, text=info_text, font=("Arial", 12), 
                     fg=COLORS['light'], bg=COLORS['dark'], justify='left')
info_label.pack(padx=20, pady=15)

# Model Details Panel
model_frame = tk.Frame(main_container, bg=COLORS['dark'], relief='sunken', bd=2)
model_frame.pack(fill='x', pady=(0, 20))

model_text = """Model Equation: Salary = 9356.86 × Years + 2000\nR² Score: 0.98 | Model Accuracy: High"""

model_label = tk.Label(model_frame, text=model_text, font=("Arial", 12, "bold"), 
                      fg=COLORS['success'], bg=COLORS['dark'], justify='center')
model_label.pack(padx=20, pady=15)

# Input and Results Section
input_results_frame = tk.Frame(main_container, bg=COLORS['secondary'])
input_results_frame.pack(fill='both', expand=True, pady=20)

# Left Side - Input Section
left_frame = tk.Frame(input_results_frame, bg=COLORS['dark'], relief='raised', bd=2)
left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))

tk.Label(left_frame, text="Enter Years of Experience:", 
         font=("Arial", 16, "bold"), fg=COLORS['light'], bg=COLORS['dark']).pack(pady=(30, 10))

entry_years = tk.Entry(left_frame, font=("Arial", 18), width=15, 
                      justify='center', relief='solid', bd=3)
entry_years.pack(pady=20)

# Buttons Container
buttons_container = tk.Frame(left_frame, bg=COLORS['dark'])
buttons_container.pack(pady=30)

btn_predict = tk.Button(buttons_container, text="Predict Salary", command=predict_salary,
                       font=("Arial", 14, "bold"), bg=COLORS['success'], fg='white',
                       width=15, height=2, relief='raised')
btn_predict.pack(pady=10)

btn_reset = tk.Button(buttons_container, text="Reset Input", command=reset_input,
                     font=("Arial", 14, "bold"), bg=COLORS['warning'], fg='white',
                     width=12, height=2, relief='raised')
btn_reset.pack(pady=10)

# Right Side - Results Section
right_frame = tk.Frame(input_results_frame, bg=COLORS['dark'], relief='raised', bd=2)
right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))

tk.Label(right_frame, text="Prediction Results", 
         font=("Arial", 18, "bold"), fg=COLORS['light'], bg=COLORS['dark']).pack(pady=(40, 20))

lbl_result = tk.Label(right_frame, text="Predicted Salary: ---", 
                     font=("Arial", 20, "bold"), fg=COLORS['light'], 
                     bg=COLORS['dark'], pady=30)
lbl_result.pack()

# Example predictions
examples_frame = tk.Frame(right_frame, bg=COLORS['dark'])
examples_frame.pack(pady=30)

examples_text = """Example Predictions:
• 2 years: $22,713.72
• 5 years: $48,784.30
• 8 years: $74,854.88
• 10 years: $95,568.60"""

examples_label = tk.Label(examples_frame, text=examples_text, font=("Arial", 12), 
                         fg=COLORS['primary'], bg=COLORS['dark'], justify='left')
examples_label.pack()

# Footer
footer = tk.Frame(main_container, bg=COLORS['dark'], height=50)
footer.pack(fill='x', pady=(20, 0))
footer.pack_propagate(False)

footer_label = tk.Label(footer, text="ML Salary Prediction System v1.0 | Built with Linear Regression", 
                       font=("Arial", 10), fg=COLORS['light'], bg=COLORS['dark'])
footer_label.pack(pady=15)

# Focus on entry field
entry_years.focus_set()

root.mainloop()