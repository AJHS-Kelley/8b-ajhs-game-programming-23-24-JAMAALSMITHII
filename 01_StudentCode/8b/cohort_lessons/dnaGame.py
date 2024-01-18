# DNA Replication Game, Jamaal Smith, V0.0

# Import Entire Modules -- Get the whole tool box 
import time, datetime

# Import Specific Methods -- Get the specific tool 
from random import choice

# Store the DNA Bases 
dnaBases = ["A", "T", "G", "C"]

# GAME FUNCTIONS
def gameIntro() -> None:
    pass 

def genDNA() -> str: 
    basesGenerated = 0 
    basesRequested = int(input("Please enter a positive integer number of bases to generate. \n"))
    dnaSequence = ""
    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence

def DoTranscription(dnaSquence:str) -> tuple:
    
    print(f"The DNA Sequence is {dnaSquence}. \n")
    print("You will now generate the RNA squence that would match . \n")
    print("Please remember, in the RNA squence U pairs with A from the DNA squence. \n")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan. 01, 1970
    rnaSequence = input("Please enter the matching RNA sequence. Leave no spaces! Then press enter. \n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime)
# Tuples are ORDERED -- you can reference elements with the index. 
# Tuples are UNCHANGEABLE -- you cannot add, modify, or delete after creatiing tuple
# Tuples CAN have duplicate values.

def verifySequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False 
    if len(dnaSequence) != len(rnaSequence):
        print("The sequences are different lengths and cannot match. \n")
        return isMatch
    for dnaBase, rnaBase in zip(dnaSequence, rnaSequence):
        if dnaBase == "A" and rnaBase == "U":
            isMatch = True
        elif dnaBase == "C" and rnaBase == "G":
            isMatch = True
        elif dnaBase == "G" and rnaBase == "C":
            isMatch = True
        elif dnaBase == "T" and rnaBase == "A":
            isMatch = True
        else:
            print("Unable to identify correct base so no match. \n")
    return isMatch

def calcScore(rnaSequece: str, rnaTime: float) -> int:
    score = 0
    if rnaTime < 1.0: # Fastest Time, Highest Score
        score += 1000000
    elif rnaTime < 5.0:
        score += 900000
    elif rnaTime < 15.0:
        score += 700000
    elif rnaTime < 25.0:
        score += 500000
    else: # Slowest Time, Lowest Score
        score += 25000
    return score 

scoreMulti = 0.0
    if len(rnaSequence) >= 30: # Longest Sequence, Highest Multiplier
        scoreMulti = 5.0
    elif len(rnaSequence) >= 25: # Longest Sequence, Highest Multiplier
        scoreMulti = 4.0
    elif len(rnaSequence) >= 20: # Longest Sequence, Highest Multiplier
        scoreMulti = 3.0
    elif len(rnaSequence) >= 15: # Longest Sequence, Highest Multiplier
        scoreMulti = 2.0
    elif len(rnaSequence) >= 5: # Longest Sequence, Highest Multiplier
        scoreMulti = 1.0
    else: # Shorest Sequence, Loest Multiplier 
        scoreMulti = 0.5
    # Increase score, multiplier should be > 1.0
    # Decrease scpre, multiplier should be < 1.0
    score *= scoreMulti
    return score 
def saveScore(dnaSequence: str, rnaSequence: str, rnaTime : float) -> None:
    playerName = input("What is your first name? \n")
    lastName = input("What is your last name ? \n")
    fullName = playerName + " " + lastName

    fileName = "dnaReplicationScore" + fullName + ".txt"

    saveData = open(fileName, "a")
    # File Modes
    # "x" mode -- CREATE FILE, IF FILE EXISTS, EXIT WITH ERROR
    # "w" mode -- CREATE FILE, IF FILE EXISTS, OVERWRITE IT
    # "a" mode -- CREATE FILE, IF FILE EXISTS, APPEND TO IT
    saveData.write(f"DNA Sequence: {dnaSequence}\nRNA Sequence: {rnaSequence}\n")
    saveData.write(f"Transcription Time: {rnaTime}\n")
    saveData.write(f"Score: {score}\n")
    saveData.write(f"{fullName}\n")
    saveData.write(f"{datetime.datetime.now()}\n")
    saveData.close()

dna = genDNA()
rna = DoTranscription(dna)
print(verifySequence(dna, rna[0]))

print(calcScore(rna[0], rna[1]))
    