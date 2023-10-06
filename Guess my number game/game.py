import random
import shutil


def print_heading(text):  # This function designs and aligns the heading in the center
    width = shutil.get_terminal_size().columns
    padding = (width-len(text))//2
    print(f"{'='*padding}{text}{'='*padding}")


print_heading(" GUESS THE NUMBER ")
while True:  # This while is used to make an odd loop
    x = int(input("Enter the starting point: "))
    y = int(input("Enter the ending point: "))
    randNumber = random.randint(x, y)
    userGuess = None
    playAgain = None
    # print(randNumber)                              (Faizan has included this line for testing purpose)
    while (userGuess != randNumber):
        try:
            userGuess = int(input("Enter your guess: "))
            if (userGuess == randNumber):
                print("You guessed it right.")
                # This is to stimulate odd loop
                playAgain = input(
                    "Wanna play again?(Press (\"N\" or \"n\") for \"No\", and any other key for \"Yes\"): ")
            elif (userGuess >= randNumber):
                print("You guessed a greater number, try a smaller number.")
            elif (userGuess <= randNumber):
                print("You guessed a smaller number, try a greater number.")
        except:
            # If user enters a value other than a number
            print("Enter a valid number.")
    if (playAgain == "N" or playAgain == "n"):  # This decides the execution of odd loop
        break
#PROJECT MADE BY : FAIZAN ASHRAF
# ROLL NUMBER :18 