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

# shotContested is the defender contesting your shot. Depending on their defensive level they could either make your shot harder to make or make no difference at all.
# Having a good shotRelease will help you make more of your shots the higher your shotRelease is the more likely you are of making the shot. A 100 shotRelease will score no matter the level of the defenders contest.
def shootBall(shotContested, shotRelease):
    if shotContested > 3.0 and shotRelease <= 75:
        shotMade = True
    elif shotContested <= 3.0 and shotRelease > 65:
        shotMade = False
    else:
        print('Your shot has been blocked! Turnover! /n')
        shotBlocked = True
        return shotBlocked
    return shotMade

# You are playing defense and trying to take the ball away from the dribbler/opponent.
# Inability in stealing the ball will result in a reaching foul on you, the defender.
def stealBall(speed, strength):
    if speed <= 80 and strength <= 3.0:
        ballStole = True
    elif speed > 75 and strength >= 2.0:
        ballStole = False
    else:
        print('*Whistle* Reaching Foul! Opponents ball. /n')
        foulBall = True
        return foulBall
    return ballStole

        
    

    