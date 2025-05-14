import tkinter as tk

def convert():
    inches = float(entry.get())
    centimeters = inches * 2.54
    result_label.config(text=f"{centimeters:.2f} cm")

root = tk.Tk()
root.title("Inches to Centimeters Converter")

entry_label = tk.Label(root, text="Enter length in inches:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()