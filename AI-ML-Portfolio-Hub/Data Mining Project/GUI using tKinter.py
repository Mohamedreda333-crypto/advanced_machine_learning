#My Name : Mohamed Reda Ramadan Khamis
#Phone Number: 01554725661
#########################################################################################################################

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

# Load datasets
X_df = pd.read_csv("X_df.csv")
house_price = pd.read_csv("house_price.csv")


class Am_ML:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("House Price Prediction")
        self.root.configure(bg="Light Yellow")

        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")

        # Title
        title = Label(
            self.root,
            text="House Price Prediction",
            font=("times new roman", 40, "bold"),
            bg="#010c48",
            fg="white",
            anchor="w",
            padx=20
        )
        title.place(x=0, y=0, relwidth=1, height=70)

        # Clock
        self.lbl_clock = Label(
            self.root,
            text=f"Welcome to House Price Prediction \t\t Date: {current_date} \t\t Time: {current_time}",
            font=("times new roman", 15, "bold"),
            bg="red",
            fg="white"
        )
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # Logout Button
        btn_logout = Button(
            self.root,
            text="Logout",
            font=("times new roman", 15, "bold"),
            bg="yellow",
            cursor="hand2",
            command=self.logout
        )
        btn_logout.place(x=1150, y=10, height=50, width=150)

        # Image Frame
        image_frame = LabelFrame(
            self.root,
            text="Some pictures of houses",
            font=("times new roman", 16, "bold"),
            bg="Yellow",
            fg="black"
        )
        image_frame.place(x=875, y=120, width=400, height=550)

        self.img_1 = PhotoImage(file="C:/Users/pc/OneDrive - Benha University (Faculty Of engineering)/Desktop/Data mining project/download (2).png")
        label_img1 = Label(image_frame, image=self.img_1)
        label_img1.pack(pady=10)

        self.img_2 = PhotoImage(file="C:/Users/pc/OneDrive - Benha University (Faculty Of engineering)/Desktop/Data mining project/Image_2.png")
        label_img2 = Label(image_frame, image=self.img_2)
        label_img2.pack(pady=10)

        self.img_3 = PhotoImage(file="C:/Users/pc/OneDrive - Benha University (Faculty Of engineering)/Desktop/Data mining project/Image_3.png")
        label_img3 = Label(image_frame, image=self.img_3)
        label_img3.pack(pady=10)

        # Input Frame
        frame1 = LabelFrame(
            self.root,
            text="Input Features",
            font=("times new roman", 16, "bold"),
            bg="White",
            fg="black"
        )
        frame1.place(x=20, y=120, width=400, height=550)

        Label(frame1, text="Enter Features:", font=("times new roman", 14)).place(x=10, y=20)

        self.feature_entries = {}
        self.features = X_df.columns.tolist()

        y_offset = 60
        for feature in self.features:
            Label(frame1, text=f"{feature}:", font=("times new roman", 12, "bold")).place(x=10, y=y_offset)
            entry = Entry(frame1, font=("times new roman", 12, "bold"), bg="red", width=25)
            entry.place(x=150, y=y_offset)
            self.feature_entries[feature] = entry
            y_offset += 40

        # Model Frame
        frame2 = LabelFrame(
            self.root,
            text="Model Selection",
            font=("times new roman", 16, "bold"),
            bg="#010c48",
            fg="white"
        )
        frame2.place(x=450, y=120, width=400, height=200)

        Label(frame2, text="Choose Model:", font=("times new roman", 14, "bold")).place(x=10, y=20)

        self.model_var = StringVar()
        self.model_combobox = ttk.Combobox(
            frame2,
            textvariable=self.model_var,
            font=("times new roman", 14, "bold"),
            state="readonly"
        )
        self.model_combobox['values'] = ("Decision Tree", "Naive Bayes", "SVM", "Random Forest", "KNN")
        self.model_combobox.place(x=10, y=60, width=200)

        Button(
            frame2,
            text="Predict Price",
            font=("times new roman", 16, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2",
            command=self.predict_price
        ).place(x=10, y=120, width=150, height=40)

        # Output Text Box
        self.output_text = Text(self.root, font=("times new roman", 14), bg="white", fg="black")
        self.output_text.place(x=450, y=340, width=400, height=330)

    def predict_price(self):
        try:
            input_data = {}
            for feature, entry in self.feature_entries.items():
                value = entry.get()
                if value == "":
                    messagebox.showerror("Error", f"Please enter a value for {feature}.")
                    return
                try:
                    input_data[feature] = float(value)
                except ValueError:
                    messagebox.showerror("Error", f"Please enter a valid numeric value for {feature}.")
                    return

            X = X_df
            y = house_price.values.ravel()

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model_name = self.model_var.get()
            if model_name == "Decision Tree":
                model = DecisionTreeClassifier()
            elif model_name == "Naive Bayes":
                model = GaussianNB()
            elif model_name == "SVM":
                model = SVC()
            elif model_name == "Random Forest":
                model = RandomForestClassifier()
            elif model_name == "KNN":
                model = KNeighborsClassifier()
            else:
                messagebox.showerror("Error", "Please select a model.")
                return

            model.fit(X_train, y_train)
            input_df = pd.DataFrame([input_data])
            prediction = model.predict(input_df)[0]

            self.output_text.delete("1.0", END)
            self.output_text.insert(END, f"Model: {model_name}\n")
            self.output_text.insert(END, f"Predicted House Price: {prediction}\n")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Am_ML(root)
    root.mainloop()
