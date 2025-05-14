import tkinter as tk
from datetime import date

def calculate_age():
    d = int(day_entry.get())
    m = int(month_entry.get())
    y = int(year_entry.get())
    today = date.today()
    age = today.year - y - ((today.month, today.day) < (m, d))
    result_label.config(text=f"Age: {age} years")

root = tk.Tk()
root.title("Age Calculator")

label_day = tk.Label(root, text="Day")
label_day.grid(row=0, column=0)
day_entry = tk.Entry(root)
day_entry.grid(row=0, column=1)

label_month = tk.Label(root, text="Month")
label_month.grid(row=1, column=0)
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1)

label_year = tk.Label(root, text="Year")
label_year.grid(row=2, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1)

calc_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Age: ")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()