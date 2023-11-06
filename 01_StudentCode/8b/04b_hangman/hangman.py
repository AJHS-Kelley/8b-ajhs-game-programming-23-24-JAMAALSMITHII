# Hangman Game by Jamaal Smith II, v0.0
import random
#words = 'run ran rock roll lean drank vamp black opium purple blurple golden destroy autumn rocket breakfast wafflestomper '.split()
# DICTIONARY VERSION
# Stored in Key:Value Pairs.
# Actual Dictionary Word (Key) : Value (Definition)
# Uses {} to specify a dictionary.

words = {'Colors': 'red orange yellow green blue indigo violet fuschia teal garnet silver gold brown white blurple'.split(),
        'Animals': 'cat dog cow pig chicken mouse lion cheetah tiger snake duck goose alligator fish wombat shark bear'.split(),
        'Shapes': 'square circle triangle rhombus trapezoid diamond dodecahedron parallelogram'.split(),
        'foods': 'hamburger hotdog peanut cookies sandwich potato lettuce spinnach noodles waffle pancake fries onion chips oyster clams steak bread'.split(),}

# VARIABLE_NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
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
    ========''', '''
    +---+
    o   |
  o-|-o |
   / \  |
    ========''','''
    +---+
    o   |
  o-|-o |
   / \  |
  o  o  |
    ========''',]

# Pick Word from List
# def getRandomWord(wordList): # Return a random word from the list.
#     wordIndex = random.randint(0, len(wordlist) - 1)
#     # len(listNmae) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS
#     return wordList[wordIndex]

# Pick Word from Dictionary
def getRandomWord(wordDict): # Return a random word from the list.
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey] - 1))
    return [wordDict[wordKey][wordIndex], wordKey]

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
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
             print('Please guess a LETTER from the English alphabet.')
        else:
            return guess
        
def playAgain():
    print('Do you want to play again? Yes or No?')
    return input().lower().startswith('y')

# Introduce the Game
print('We are playing hangman')

# CHOOSE DIFFICULTY
difficulty = 'X'
while difficulty not in 'EMH':
    print('Please choose Easy, Medium or Hard. Type the first letter then press enter \n')
    difficulty = input().upper()
if difficulty =='M': # MEDIUM
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
if difficulty =='M': # HARD
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
    del HANGMAN_BOARD[5]
    del HANGMAN_BOARD[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words) 
gameIsDone = False

# Main Game Loop
while True:
    print('The secret wword is from the ' + secretSet + ' category. \n')
    display(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess 

        # Check To See If Winnerm Winner Chicken Dinner
        foundAllLetters = True 
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters: 
                foundAllLetters = False
                break
        if foundAllLetters: #if True:
            print('You are incredible!')
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
