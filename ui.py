import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from macronutrientcalc import bmrcalc, check_body_parameters


def calculate():
    try:
        date_string = entry_birthday.get()
        birthday = datetime.strptime(date_string, "%m/%d/%Y")
        today = datetime.today()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

        sex = entry_sex.get().upper()
        weight = int(entry_weight.get())
        height = int(entry_height.get())
        activity_factor = float(entry_activity.get())

        if not check_body_parameters(age, sex, weight, height):
            messagebox.showerror("Error", "Invalid body parameters. Please check the values and try again.")
            return

        bmr, _ = bmrcalc(age, sex, weight, height)

        if activity_factor not in [1.2, 1.375, 1.55, 1.75]:
            messagebox.showerror("Error", "Activity factor must be one of the following: 1.2, 1.375, 1.55, 1.75.")
            return

        daily_calories = bmr * activity_factor

        messagebox.showinfo("Result",
                            f"Your BMR is {bmr} kcal \nYour daily calorie needs are {round(daily_calories, 2)} kcal")

    except ValueError as ve:
        messagebox.showerror("Error", f"Invalid input: {ve}")


root = tk.Tk()
root.title("Calorie and Macronutrient Calculator")


tk.Label(root, text="Enter your birthday (MM/DD/YYYY):").grid(row=0, column=0, padx=10, pady=5)
entry_birthday = tk.Entry(root)
entry_birthday.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter your sex (M/F):").grid(row=1, column=0, padx=10, pady=5)
entry_sex = tk.Entry(root)
entry_sex.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter your weight (kg):").grid(row=2, column=0, padx=10, pady=5)
entry_weight = tk.Entry(root)
entry_weight.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Enter your height (cm):").grid(row=3, column=0, padx=10, pady=5)
entry_height = tk.Entry(root)
entry_height.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Enter your activity factor (1.2, 1.375, 1.55, 1.75):").grid(row=4, column=0, padx=10, pady=5)
entry_activity = tk.Entry(root)
entry_activity.grid(row=4, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=5, columnspan=2, pady=10)

root.mainloop()
