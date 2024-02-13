import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.timeClock()
test_font = pygame.font.Font('font/Pixeltype.tff', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, 'Black')
score_rect = score_surf.get_rect(center = (400,50))

small_surface = pygame.image.load('graphics.snail/snail1.png').convert()
snail_rect = snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/player/player_walk_1/png').convert_alpha()
player_rect = player_surf.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #   if player_rect.collidepoin(event.pos): print('collision')

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,'Pink',score_rect)
    pygame.draw.rect(screen,'Pink',score_rect,10)
    pygame.draw.line(screen,'Gold',(0,0),(800,400),10
    screen.blit(score_surf,score_rect)
            
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)

    # if player_rect.colliderect(snail_rect):
    #   print('collision')

    # mouse_pos =pygame.mouse.get_pos()
    # if player_rect.collidepoints(mouse_pos):
    #    print(pygame.mouse.get_pressed())


    pygame.display.update()
    clock.tick(60) 