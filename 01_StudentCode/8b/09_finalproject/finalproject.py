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

    if keys[pygame.K_LEFT]: 
        player = x,y = velocity

        if keys[pygame.K_RIGHT]: 
            player = x,y = velocity

            if keys[pygame.K_UP]:
                player = x,y = velocity

                if keys[pygame.K_DOWN]:
                     player = x,y = velocity

    pygame.draw.rect(win, (255,0,0), (x, y, 1980, 1020))   
    pygame.display.update() 
    
    pygame.quit()

    # Attacking Enemies -- Determine Direction / Range / Hit % 
    

    # Picking Up / Using Items 


    # Display the Graphics
    # Use .blit() primarily 

    # DEBUGGING MESSAGES 
    print(f"Mouse: {pygame.mouse.get_pos()}\n")

    # ALWAYS LAST
    pygame.display.update()
    clock.tick(60)
















