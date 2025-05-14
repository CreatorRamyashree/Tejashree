from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry("500x500")

def msg():
    # messagebox.showwarning("Alert", "Stop! Virus found.")
    messagebox.askyesno("confirmation box", "Please select Yes or No")

button = Button(root, text = "Click here to confirm.", command=msg)
button.place(x=40, y=80)
root.mainloop()