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
# i = 0
# while i < 100:
#      word = getRandomWord(words)
#      print(word)