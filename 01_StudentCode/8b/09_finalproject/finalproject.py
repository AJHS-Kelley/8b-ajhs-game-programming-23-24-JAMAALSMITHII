# final Project, Jamaal Smith, v0.0
import sys, random, pygame


# Debugging Logs
logFile = "geometryBlasterDebugLog.txt"
logData = open(logFile, "w")

resolution = 0 # 0 = Low resolution (800 x 600), 1 = High Resolution (1920 x 1080)

if resolution == 0:
        x = 800
        y = 600
else:
        x = 1920
        y = 1080

pygame.init()
clock = pygame.time.Clock() 

Difficulty = int(input("Hello. Welcome. PLease select the game mode you would like to play. 1 for CASUAL PLAY or 2 for RANKED. \n"))

if Difficulty == 1:
    pygame.display.set_caption("FlxRR -- Casual play")
else:
    pygame.display.set_caption("FlxRR -- Ranked")

screen = pygame.display.set_mode((1920, 1080))

# Main Loop -- Start Here
while True: # Each iteration through this loop is ONE FRAME of your game. 
     
    # This loop works best for 'menu' and 'option' type events. 
    for event in pygame.event.get(): # Check to see if there are events.
        pass

    # The code from here down should happen EVERY FRAME. 

    velocity = 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Controls -- How to Move the Player? 
    keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

# Importing pygame module 

    from pygame.locals import *

# initiate pygame and give permission 
# to use pygame's functionality. 
    pygame.init() 

# create the display surface object 
# of specific dimension. 
    window = pygame.display.set_mode((600, 600)) 

# Add caption in the window 
    pygame.display.set_caption('Player Movement') 

# Add player sprite 
    image = pygame.image.load(r'Player_image.png') 


# Store the initial 
# coordinates of the player in 
# two variables i.e. x and y. 
    x = 100
    y = 100

# Create a variable to store the 
# velocity of player's movement 
    velocity = 12

# Creating an Infinite loop 
    run = True
    while run: 

	# Filling the background with 
	# white color 
	    window.fill((255, 255, 255)) 

	# Display the player sprite at x 
	# and y coordinates 
window.blit(image, (x, y)) 

	# iterate over the list of Event objects 
	# that was returned by pygame.event.get() 
	# method. 
for event in pygame.event.get(): 
	Setup

backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10


Main; Loop
 

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)

    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)