import random

def play_game():
    print("Welcome to Rock Paper Scissors!")
    choices = ["rock", "paper", "scissors"]
#this just imports the random module to generate anything random and the code says " welcome to rock paper scissors and shows you your choices"
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
# this is a simple loop that asks the user to input their choice and checks if it is valid they can continue or if it is invalid they can try again
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
#this generates a random choice for the computer and prints it out after the user has made their choice
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
# this determines the winner pretty much by checking the outcome in the rules

play_game() # this just runs the function which i defined at the start


