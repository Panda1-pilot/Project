import random
import tkinter as tk
from tkinter import messagebox

def play_game(user_choice):
    computer_choice = random.choice(choices)
    result_text = ""

    if user_choice == computer_choice:
        result_text = "It's a draw!"
        results[2] += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result_text = f"You win! Computer chose {computer_choice}."
        results[0] += 1
    else:
        result_text = f"Computer wins! Computer chose {computer_choice}."
        results[1] += 1

    messagebox.showinfo("Result", result_text)
    update_score()

def update_score():
    score_label.config(text=f"Wins: {results[0]}  Losses: {results[1]}  Draws: {results[2]}")

def quit_game():
    messagebox.showinfo("Game Over", f"Final Scores:\nWins: {results[0]}\nLosses: {results[1]}\nDraws: {results[2]}\nThanks for playing, {user_name}")
    root.destroy()

# Game setup
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

results = [0, 0, 0]  # Wins, Losses, Draws
choices = ["rock", "paper", "scissors"]

# Welcome screen
welcome_label = tk.Label(root, text="Welcome to Rock, Paper, Scissors!", font=("Arial", 16))
welcome_label.pack(pady=10)

name_label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
name_label.pack()

name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

# Game controls
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

def start_game():
    global user_name
    user_name = name_entry.get().strip()
    if not user_name:
        messagebox.showwarning("Input Error", "Please enter your name to start the game.")
        return

    name_label.pack_forget()
    name_entry.pack_forget()
    start_button.pack_forget()

    instruction_label = tk.Label(root, text=f"Hi {user_name}, choose your move:", font=("Arial", 12))
    instruction_label.pack(pady=5)

    for choice in choices:
        btn = tk.Button(button_frame, text=choice.capitalize(), font=("Arial", 12), command=lambda c=choice: play_game(c))
        btn.pack(side=tk.LEFT, padx=10)

    quit_button = tk.Button(root, text="Quit", font=("Arial", 12), command=quit_game)
    quit_button.pack(pady=10)

    global score_label
    score_label = tk.Label(root, text=f"Wins: {results[0]}  Losses: {results[1]}  Draws: {results[2]}", font=("Arial", 12))
    score_label.pack()

start_button = tk.Button(root, text="Start Game", font=("Arial", 12), command=start_game)
start_button.pack(pady=10)

root.mainloop()
