# Example Game Functions Project, Ryan Kelley, v0,1
import random

def functionOne():
    pass

def functionTwo(param1):
    pass

def functionThree(param1 = "Default Value"):
    pass

def functionFour(param1, param2, param3): 
    pass

def shootBall(shotContested, shotRelease):
    if shotContested > 3.0 and shotRelease <= 75:
        shotMade = True
    elif shotContested > 2.0 and shotRelease > 65:
        shotMade = False
    else:
        print('Your shot has been blocked! Turnover! /n')
        shotBlocked = True
        return shotBlocked
    return shotMade

def stealball(speed, strength):
    if speed <= 80 and strength <= 3.0:
    

    