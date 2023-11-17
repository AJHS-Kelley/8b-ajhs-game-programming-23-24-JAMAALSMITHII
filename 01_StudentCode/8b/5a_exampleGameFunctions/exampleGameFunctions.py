# Example Game Functions Project, Ryan Kelley, v0,4
import random


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

def dunkBall(vertical, strength):
    if vertical <= 75 and strength <= 4.0:
        ballDunked = True
    elif vertical > 70 and strength > 2.0:
        ballDunked = False
    else:
        print('And he missed the dunk!! /n')
        missedDunk = True
        return missedDunk
    return ballDunked

    

    