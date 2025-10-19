import tkinter as tk
from tkinter import messagebox
import random

# Initialize main window
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x400")
root.config(bg="#1e1e2f")

# Global variables
number = 0
attempts = 0
player_name = ""

# Function to start the game
def start_game():
    global number, attempts, player_name
    player_name = name_entry.get().strip()
    if not player_name:
        messagebox.showwarning("Input Error", "Please enter your name before starting.")
        return
    number = random.randint(1, 100)
    attempts = 0
    result_label.config(text=f"Hi {player_name}, I have chosen a number between 1 and 100.\nStart guessing!")
    guess_entry.delete(0, tk.END)

# Function to check the guess
def check_guess():
    global attempts
    guess = guess_entry.get().strip()
    if not guess.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return
    guess = int(guess)
    attempts += 1

    if guess == number:
        messagebox.showinfo("Correct!", f"🎉 Correct, {player_name}!\nYou guessed it in {attempts} attempts.")
        result_label.config(text=f"Well done {player_name}! The number was {number}.")
    elif guess < number:
        result_label.config(text=f"Too low! Try again, {player_name}.")
    else:
        result_label.config(text=f"Too high! Try again, {player_name}.")

# Function to reset the game
def reset_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 0
    guess_entry.delete(0, tk.END)
    result_label.config(text=f"New number generated, {player_name}! Start guessing again.")

# ------------------ UI Design ------------------
title_label = tk.Label(root, text="🎯 Guess the Number Game 🎯", font=("Arial", 16, "bold"), bg="#1e1e2f", fg="white")
title_label.pack(pady=15)

name_label = tk.Label(root, text="Enter your name:", bg="#1e1e2f", fg="white", font=("Arial", 12))
name_label.pack()
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

start_btn = tk.Button(root, text="Start Game", font=("Arial", 12, "bold"), bg="#0078D7", fg="white", command=start_game)
start_btn.pack(pady=10)

guess_label = tk.Label(root, text="Enter your guess (1-100):", bg="#1e1e2f", fg="white", font=("Arial", 12))
guess_label.pack()
guess_entry = tk.Entry(root, font=("Arial", 12))
guess_entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Guess", font=("Arial", 12, "bold"), bg="#28a745", fg="white", command=check_guess)
check_btn.pack(pady=10)

reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 12, "bold"), bg="#ffc107", fg="black", command=reset_game)
reset_btn.pack(pady=5)

result_label = tk.Label(root, text="", bg="#1e1e2f", fg="lightgreen", font=("Arial", 12), wraplength=350)
result_label.pack(pady=15)

exit_btn = tk.Button(root, text="Exit", font=("Arial", 12, "bold"), bg="#dc3545", fg="white", command=root.destroy)
exit_btn.pack(pady=10)

# Run the main loop
root.mainloop()


