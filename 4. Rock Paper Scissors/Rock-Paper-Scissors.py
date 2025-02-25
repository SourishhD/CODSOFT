import tkinter as tk
import random


choices = ["Rock", "Paper", "Scissors"]


user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)  

   
    if user_choice == computer_choice:
        result = "It's a Tie! 🤝"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win! 🎉"
        user_score += 1
    else:
        result = "Computer Wins! 😢"
        computer_score += 1

    # Update UI with results
    result_label.config(text=f"Your Choice: {user_choice}\nComputer Choice: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Choose Rock, Paper, or Scissors!")
    score_label.config(text="Score - You: 0 | Computer: 0")

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x300")

# Labels
title_label = tk.Label(window, text="Rock, Paper, Scissors!", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

result_label = tk.Label(window, text="Choose Rock, Paper, or Scissors!", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Buttons for Rock, Paper, and Scissors
button_frame = tk.Frame(window)
button_frame.pack()

rock_button = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 12), command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="📄 Paper", font=("Arial", 12), command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="✂️ Scissors", font=("Arial", 12), command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Reset button
reset_button = tk.Button(window, text="🔄 Reset Scores", font=("Arial", 12), command=reset_game)
reset_button.pack(pady=10)

# Start the main loop
window.mainloop()
