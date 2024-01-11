# DNA Replication Game, Ryan Kelley, V0.0

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
    
dna = genDNA()

def genRNA(dnaSquence: str) -> tuple:
    
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

rna = genRNA(dna)
print(rna)
    
