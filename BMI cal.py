import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        name = name_entry.get()
        height_cm = float(height_entry.get())
        weight = float(weight_entry.get())

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
            advice = "You should eat healthy and gain weight."
        elif 18.5 <= bmi < 25:
            category = "Normal"
            advice = "You are healthy. Keep it up!"
        elif 25 <= bmi < 30:
            category = "Overweight"
            advice = "Try regular exercise and balanced diet."
        else:
            category = "Obese"
            advice = "Consult a doctor for proper guidance."

        result_label.config(
            text=f"Name: {name}\nBMI: {bmi}\nCategory: {category}\nAdvice: {advice}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x400")

# Heading
tk.Label(window, text="BMI Calculator", font=("Arial", 18, "bold")).pack(pady=10)

# Name
tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Height
tk.Label(window, text="Height (cm)").pack()
height_entry = tk.Entry(window)
height_entry.pack()

# Weight
tk.Label(window, text="Weight (kg)").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

# Button
tk.Button(window, text="Calculate BMI", command=calculate_bmi).pack(pady=15)

# Result
result_label = tk.Label(window, text="", font=("Arial", 10), fg="blue")
result_label.pack()

# Run window
window.mainloop()