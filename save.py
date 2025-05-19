from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename

from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry("500x500")

def save():
    files = [("All files", "*.*"),("Python files", "*.py"), ("Text document", "*.txt")]
    file = asksaveasfile(filetypes = files, defaultextension=files)

def open_file():
    """Open a file for editing.""" 
    filepath = askopenfilename(filetypes = [("Text files", "*.txt"), ("All files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    root.title(f"Codingal's text editor - {filepath}")

txt_edit = Text(root)
btn = Button(root, text = "Save", command = lambda: save ())
btn.pack(side = TOP)
btn2 = Button(root, text = "Open", command = lambda: open_file ())
btn2.pack(side = RIGHT)
mainloop()