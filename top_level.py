from tkinter import*
root = Tk()
root.geometry("500x500")
root.title("main")
l = Label(root, text = "This is root window.")

top = Toplevel()
top.geometry("200x180")
top.title("toplevel")
l2 = Label(top, text = "This is toplevel window.")
root.mainloop()