import pygame 
from sys import exit

# Almost finished, but you have a critical crash as soon as the code is executed.  Y
# You must fix these errors before the final submission is due!

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.timeClock()
test_font = pygame.font.Font('font/Pixeltype.tff', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

small_surface = pygame.image.load('graphics.snail/snail1.png').convert()
snail_rect = snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/player/player_walk_1/png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #   if player_rect.collidepoin(event.pos): print('collision')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')

        if event.type == pygame.KEYUP:
            print('key up')

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
    screen.blit(score_surf,score_rect)
            
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)

    # Player
    player_gravity += 1 
    player_rect.y =+ player_gravity
    screen.blit(player_surf,player_rect)

    # keys = (pygame.key.get_pressed)
    # if keys[pygame.K_SPACE]:
    #    print('jump')

    # if player_rect.colliderect(snail_rect):
    #   print('collision')

    # mouse_pos =pygame.mouse.get_pos()
    # if player_rect.collidepoints(mouse_pos):
    #    print(pygame.mouse.get_pressed())


    pygame.display.update()
    clock.tick(60) 