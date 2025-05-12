from tkinter import *
import datetime

root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

label1 = Label(text="Hey There!", fg="white", bg="#B2750B", height=1, width=30)
label1.pack()

label2 = Label(text="Click here to fill form for user details")
label2.pack()
name_entry = Entry()
name_entry.pack()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello " + name
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, str(datetime.date.today()))

text_box = Text(height=5)
text_box.pack()

btn = Button(text="Login", command=display, height=3, bg="#2136AF", fg="white")
btn.pack()
root.mainloop()