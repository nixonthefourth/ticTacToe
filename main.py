# Import of the modules
import os

# Global Variables
keys = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
         6: '6', 7: '7', 8: '8', 9: '9'}

game, complete = True, False
turn = 0
prevTurn = -1

# Functions

# Defines library we can interact with
def frameCreation(keys):
    board = (f"({keys[1]})({keys[2]})({keys[3]})\n"
             f"({keys[4]})({keys[5]})({keys[6]})\n"
             f"({keys[7]})({keys[8]})({keys[9]})")
    print(board)

# Checks the turn
def turnChecker(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'

#Checks the winner
def shikari(dict):

    # Define Horizontal Cases
    if (keys[1] == keys[2] == keys[3]) \
            or (keys[4] == keys[5] == keys[6]) \
            or (keys[7] == keys[8] == keys[9]):
        return True

    # Define Vertical Cases
    elif (keys[1] == keys[4] == keys[7]) \
            or (keys[2] == keys[5] == keys[8]) \
            or (keys[3] == keys[6] == keys[9]):
        return True
    # Define Diagonal Cases
    elif (keys[1] == keys[5] == keys[9]) \
            or (keys[3] == keys[5] == keys[7]):
        return True

    else:
        return False

# Main Program

#Name Entry
name1 = input("Wassup, player 1, what is your name?: ")
name2 = input("Hej, player 2, what is your name?: ")

# Game Loop
while game:

    # Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Draw the current Game Board
    frameCreation(keys)

    # Let the player know about an invalid turn
    if prevTurn == turn:
        print("Invalid field selected, please pick another")
    prevTurn = turn
    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your field or press 'Q' to quit")

    # Get input and make sure it's possible
    choice = input()

    # Termination
    if choice == 'q':
        game = False
    elif str.isdigit(choice) and int(choice) in keys:

        # Check the availibility of the key
        if not keys[int(choice)] in {"X", "O"}:

            # If not, update the frame and increment the turn
            turn += 1
            keys[int(choice)] = turnChecker(turn)

    # Check if the game has ended
    if shikari(keys): game, complete = False, True
    if turn > 8: game = False

# Update the frame for the last time
os.system('cls' if os.name == 'nt' else 'clear')
frameCreation(keys)

# Defines the winner
if complete:
    if turnChecker(turn) == 'X':
        print(name1, " Wins!")
    else:
        print(name2, " Wins!")
else:

    # Tie Game
    print("Sorry You Are Not A Winner")

print("Thanks for playing!")
