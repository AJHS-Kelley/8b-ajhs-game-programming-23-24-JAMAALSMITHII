# Select the secret number from a given range.
# PLayer must guess the number.
# Compare guess to the secret number.
# What happens if the guess is wrong?
    # Tell them the guess is wrong.
    # Tell them the number of guesses left.
    # Tell them if too high / too low
# What happens if the guess is right?
    # Tell them guess is correct.
    # Award a point.
# What happens if the player runs out of guesses?
    # Tell player round has been lost.
    # Award point to CPU
# Check to see if plater or CPU has >= 3 points, if so they win.

from ast import If
import random # Import the random module to our code.

# DECLARATIONS 
secretNumber = 13 
playerGuess = -1
playerScore = 0 
cpuScore = 0
numGuesses = 0 
playerName = "" 
difficulty = ""
rangeMin = 0
rangeMax = 30
numAttempts = -1 

print("""
       *~~~~~~~~~~~~~~~~~~~~~~*
       |                      |
       |    Number Guesser    |
       |    Jamaal Smith II   |
       |         2023         |
       *~~~~~~~~~~~~~~~~~~~~~~*

    """)

# CPU SECRET NUMBER GENERATOR 


# GAME LOOP
print("You need to guess a number from 0 to 30. You have four guesses.\n")


# ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH ROUND
# print() an explanation of your three difficulty levels
# Use input() to store difficulty in difficulty variable.
# assign values to numAttempts, rangeMin, and rangeMax based on choice.

while playerScore != 3 and cpuScore != 3: # START THE MATCH (GAME)
    # Difficulty code needs to be BEFORE the round starts.
    # pass -- Tells Python to skip this block of code.
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}. \n")
    secretNumber = random.randint(rangeMin, rangeMax)
    # Whenever you assin a specific value to something, it's called "hard coded".
    #print (secretNumber)
    # ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH ROUND.
    # Difficulty levels go 1-3
    difficulty = input("What difficulty would you like to select?")
    if difficulty == "Easy":
        print("This is easy mode, you have 2 guesses to guess a number 1-10")
        numGuesses = 2
        rangeMin = 1
        rangeMax = 10
    elif difficulty == "Medium":
        print("This is medium mode, you have 5 guesses for numbers 1-20") 
        numGuesses = 5
        rangeMin = 1 
        rangeMax = 20
    elif difficulty == "Hard":
        print("This is hard mode, you have 4 guesses to guess a number 1-30")
        numGuesses = 4
        rangeMin = 1
        rangeMax = 30 
    else: 
        print("You didn't submit an available level, were you going to pick medium by default?")
        numGuesses = 5 
        rangeMin = 1
        rangeMax = 20 
    secretNumber = random.randint(rangeMin, rangeMax)

    numGuesses = 0
    for guesses in range(4): # START THE ROUND!
        # PUT DIFFICULTY CODE
        print(f"You have {4 - numGuesses} guesses remaining. \n")
        playerGuess = int(input(f"Type a number from {rangeMin} to {rangeMax} and press ENTER. \n"))
        # input() saves all data as a STRING by default.
        #int() will convert to an INTEGER
        # float() will convert to a FLOAT
        print(f"You have chosen {playerGuess}. Let's see if you're right! \n")
        if playerGuess == secretNumber:
            print("Holy Moly man, what a guess! You got it! \n")
            playerScore += 1 
            break # IMMEDIATELY EXIT ANY LOOP YOU ARE IN!
        else:
            print("You did not guess correctly. \n")
            if playerGuess > secretNumber:
                print("Your guess is too high. \n")
            else:
                print("Your guess is too low. \n")
        numGuesses += 1 
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU wins a point since you ran out of guesses. \n")
if playerScore >= 3:
    print("You scored 3 points first. Guess you're just a better player.\n")
else:
    print("Lmfaoo nah what how you lose to a computer.\n")