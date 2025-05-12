from tkinter import *

window = Tk()
window.title("Sample Frame")
window.geometry("200x300")

border_effects = [FLAT, SUNKEN, RAISED, GROOVE, RIDGE]
 
for r in border_effects:
    frame = Frame(master= window, relief = r, borderwidth = 5)
    frame.pack(side = LEFT)
    label = Label(master = frame, text = r)
    label.pack()
window.mainloop()