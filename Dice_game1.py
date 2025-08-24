import random
# random module is imported to generate anything random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# Loop until a valid number of players is entered
while True:
    try:
        players = int(input("Enter the number of players: "))
        if 2 <= players <= 4:
            print("Lets roll the dice!")
            break
        else:
            print("Invalid number of players, please enter a number between 2 and 4:")
    except ValueError:
        print("Please enter a valid integer.")

scores = [0] * players
current_player = 0 # Start with Player 1


while True:
    print(f"Current player: Player {current_player + 1}")
    function = input('Press "r" to roll the dice: ')
    if function.lower() == "r":
        value = roll()
        print(f"You rolled a {value}")
        # End game if Player 4 rolls a 1
        if current_player == 3 and value == 1:
            print("Player 4 rolled a 1! Game over.")
            break
        if value == 1:
            print("You rolled a 1! Turn over.")
            current_player = (current_player + 1) % players
        else:
            scores[current_player] += value
        print("Scores:", scores)
    else:
        print(" dumb ahh, try again")

# After the loop, print final scores
print("Final scores:")
for i, score in enumerate(scores):
    print(f"Player {i+1}: {score}")

# this was torture to write, but I did it
