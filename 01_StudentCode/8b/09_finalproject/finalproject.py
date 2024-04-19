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

screen = pygame.display.set_mode((x, y))


# def startgame():
#    content 
#    def button(x,y,w,h):
#     pos = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()

#     if pos[0] > x and pos[0] < x + w and pos[1] > y and pos[1] < y + h:
#        if click[0] == 1:
#          startgame()
#     pygame.draw.rect(screen, color, (x,y,w,h))

# def menu():

#         while True:

#         surface.blit(background, (0, 0))


#         button(x,y,w,h)

#         for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         pygame.display.update()

# Main Loop -- Start Here
while True: # Each iteration through this loop is ONE FRAME of your game. 
     
    # This loop works best for 'menu' and 'option' type events. 
    for event in pygame.event.get(): # Check to see if there are events.
        pass

    # The code from here down should happen EVERY FRAME. 

    
    # Controls -- How to Move the Player? 


    # Attacking Enemies -- Determine Direction / Range / Hit % 
    

    # Picking Up / Using Items 


    # Display the Graphics
    # Use .blit() primarily 

    # DEBUGGING MESSAGES 
    print(f"Mouse: {pygame.mouse.get_pos()}\n")

    # ALWAYS LAST
    pygame.display.update()
    clock.tick(60)