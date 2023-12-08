# Example Game Functions Project, Ryan Kelley, v0,4
import random

random.randint

# shotContested is the defender contesting your shot. Depending on their defensive level they could either make your shot harder to make or make no difference at all.
# Having a good shotRelease will help you make more of your shots the higher your shotRelease is the more likely you are of making the shot. A 100 shotRelease will score no matter the level of the defenders contest.
def shootBall(shotContested, shotRelease):
    if shotContested > 3.0 and shotRelease <= 75:
        shotMade = True
    elif shotContested <= 3.0 and shotRelease > 65:
        shotMade = False
    else:
        print('Your shot has been blocked! Turnover! \n')
        shotBlocked = True
        return shotBlocked
    return shotMade

shootBall()


# You are playing defense and trying to take the ball away from the dribbler/opponent.
# Inability in stealing the ball will result in a reaching foul on you, the defender.
def stealBall(speed, strength):
    if speed <= 80 and strength <= 3.0:
        ballStole = True
    elif speed > 75 and strength >= 2.0:
        ballStole = False
    else:
        print('*Whistle* Reaching Foul! Opponents ball. \n')
        foulBall = True
        return foulBall
    return ballStole

stealBall()


def dunkBall(vertical, strength):
    if vertical <= 75 and strength <= 4.0:
        ballDunked = True
    elif vertical > 70 and strength > 2.0:
        ballDunked = False
    else:
        print('And he missed the dunk!! \n')

        missedDunk = True
        return missedDunk
    return ballDunked

dunkBall(50, 5.0)


def jumpBall(vertical):
    if vertical > 80:
        ballWon = True # Swap with Line 48
        print("WIN JUMPBALL MESSAGE HERE")
    elif vertical <= 80:
        ballWon = False # Swap with Line 46 
    
    # Greater than 80 = win the jump ball.  if vertical > 80
    # At least 50 but less than 80 = 50% chance to win the jump ball.  elif vertical > 50 
    # Less than 50 = lose the jump ball. else:  


# Code Review by Alexandra Sculley

jumpBall(50)
jumpBall(100)
