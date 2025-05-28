import tkinter as tk
import random

def determine_winner(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")

app = tk.Tk()
app.title("Rock Paper Scissors Game")
app.geometry("400x300")
app.resizable(False, False)

heading = tk.Label(app, text="Rock Paper Scissors", font=("Arial", 20, "bold"))
heading.pack(pady=10)

result_label = tk.Label(app, text="", font=("Arial", 14))
result_label.pack(pady=20)

button_frame = tk.Frame(app)
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: determine_winner("Rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: determine_winner("Paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, font=("Arial", 12), command=lambda: determine_winner("Scissors"))

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

app.mainloop()