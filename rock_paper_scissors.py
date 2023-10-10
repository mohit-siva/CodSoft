import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to update scores and display the result
def play_game():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Result: {result}")
    
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Create a Tkinter window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Label and Radio Buttons for user's choice
choice_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
choice_label.pack()

user_choice_var = tk.StringVar()
user_choice_var.set("rock")

rock_radio = tk.Radiobutton(root, text="Rock", variable=user_choice_var, value="rock")
paper_radio = tk.Radiobutton(root, text="Paper", variable=user_choice_var, value="paper")
scissors_radio = tk.Radiobutton(root, text="Scissors", variable=user_choice_var, value="scissors")

rock_radio.pack()
paper_radio.pack()
scissors_radio.pack()

# Play Button
play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

# Result and Score Labels
result_label = tk.Label(root, text="Result:")
result_label.pack()

user_score_label = tk.Label(root, text="Your Score: 0")
user_score_label.pack()

computer_score_label = tk.Label(root, text="Computer Score: 0")
computer_score_label.pack()

# Start the Tkinter main loop
root.mainloop()
