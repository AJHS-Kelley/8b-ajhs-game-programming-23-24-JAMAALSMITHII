# final Project, Jamaal Smith, v0.0
import sys, random, pygame

resolution = 0 # 0 = Low resolution (800 x 600), 1 = High Resolution (1920 x 1080)

    if resolution == 0:
        x = 800
        y = 600
    else:
        x = 1920
        y = 1080

pygame.init()

Difficulty = int(input("Hello. Welcome. PLease select the game mode you would like to play. 1 for CASUAL PLAY or 2 for RANKED. \n"))

if Difficulty == 1:
pygame.display.set_caption("FlxRR -- Casual play")
else:
pygame.display.set_caption("FlxRR -- Ranked")

screen = pygame.display.set_mode((x, y))
screen = pygame.display.set_mode((x, y))
