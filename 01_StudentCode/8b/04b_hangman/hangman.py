# Hangman Game by Jamaal Smith II, v0.0
import random
words = 'run ran rock roll lean drank vamp black opium purple blurple golden destroy autumn wafflestomper '.split()

# VARIABLE_NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = [' ' '
    +---+
        |
        |
        |
    ======== ''', '''
    +---+
    o   |
        |
        |
    ======== ''', '''
    +---+
    o   |
    |   |
        |
    ======== ''', '''
    +---+
    o   |
   /|   |
        |
    ======== ''', '''
    +---+
    o   |
   /|\  |
        |
    ======== ''', '''
    +---+
    o   |
   /|\  |
   /    |
    ======== ''', '''
    +---+
    o   |
   /|\  |
   / \  |
    ======== ''', ''']

# Pick Word from List
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0, len(wordlist) - 1)
    # len(listNmae) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS
    return wordList[wordIndex]

def display(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()
    
    blank = '_' * len(secretWord)

    # Replace Blanks with Correct Letters 
    for i in range (len(secretWord)):
        if secretWord [i] in correctLetters: 
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:] 

    for letter in blanks: 
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True: 
        print('Please guess a letter and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed: 
            print('Letter has been guessed alreadym try again.')
        elif guess not on 'abcdefghijklmnopqrstuvwxyz':
             print('Please guess a LETTER from the Englush alphabet.')
        else:
            return guess
        
def playAgain():
    print('Do you want to play again? Yes or No?')
    return input().lower().startswith(y)

# Introduce the Game
print('We are playing hangman')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

# Main Game Loop
while True:
    display(missedLetters, correctLetters, secretWord)

    guess = getGuessed(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess 

        # Check To See If Winnerm Winner Chicken Dinner
        foundAllLetters = True 
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters: 
                foundAllLetters = False
                break
            if foundAllLetters:
                print('You are incredible!!! (you got lucky...)')
            print('The secret word was' + secretWord)
            gameIsDone = True 
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
              display(missedLetters, correctLetters, secretWord)
              print('You have run out of guesses and lost the game, LOSERRR')
              print('You made this number f correct guesses' + str(len(correctLetters)))
              print('The secret word was' +secretWord)
              gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break 
    
    




# i = 0
# while i < 100:
#      word = getRandomWord(words)
#      print(word)
