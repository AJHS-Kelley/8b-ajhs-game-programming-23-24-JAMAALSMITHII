# Data type and Operators, Jamaal Smith, v0.3

# Variable Rules.
# Can not start with a number 
# Can not use built in keywords as variables.
# Varaible name should describe data being stored.
# snake_case variables use _ to seperate words, all lowercase
# camelcase variables do not use spaces, 1st word lowser, rest upper
#
# String Literal Exanples
playerName = "Monkey D. Luffy" 
emptyString = " "
spaceString = " "
monsterName = "Kizaru"

# Integer Data Types
health = 500
ExtraLives = 3
Temperature = 75

1# Floating Point Data Types
pi = 3.14167
lapTime = 1.7 
velocity = 2.21

# Bolean Data Types
isFireType = True 
WeaponEquipped = True
pvpEnabled = True 

# Arithemetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH
print[3+-1] # Addition 
print[0-17] # Substraction 
print[2*-5] # Multiplication 
print[3/-2] # Division
print[3 ** 9] # Exponent 
print[19%6] # Modulus -- Divides, then returns remander

# Compparison Operators 
# Evalute The Expression Then Return True Or False
print (5 > 3) # Greater than 
print (7 >= 2) # Greater than or equal too
print (7 < 10) # Less than 
print (5 <= 5) # Less than or equal too 
print (4 == 4) # Is Equal to
print (56 != 78) # Not equal to

# Assignment Operators
myVariables = "myValue" # Assign variable on the left the value on the right, throw out my current value

myVariableAgain = 1
myVariableAgain = 5
print(myVariableAgain)

# Addition Aassignment
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet)

# Same Effect
x = 0
x += 1 
x = x + 1

# Logical Operators
print(3 > 5 and 4 < 3) #AND requires ALL expressions to be True.
print(3 > 2 and 4 < 3)
print(3 > 2 and 4 != 3)
print(3 > 2 and 4 != 3 and favColor == "Blue" and temp == -5)
# When writing and expressions, put the value most likely to be False first!

# Logical OR -- Requires ONE expression to be true.
Print(5 > 2 or 2 < -2) 
print(3 != 3 or 5 == 5) 

# AND OR Combined
print("Line 81")
print(3 > 2 and 4 > 3 and 5 != 7) 
print(True and False or True)
# print (True and False and True)

# NOT Logical Operator
print (not (3 > 2))
print(not (not (not (5 != 3)))) 