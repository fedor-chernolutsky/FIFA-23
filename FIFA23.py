# -*- coding: utf-8 -*-
import pygame
pygame.init()

screen = pygame.display.set_mode()
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

choplin = pygame.font.Font("Choplin-Medium.ttf", 12)

logo = pygame.image.load("FIFA23.png")
alpha = 0
you_can_go_to_the_next_scene = False
going_to_the_next_scene = False


while True:
    clock.tick(FPS)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            quit()
        
        if event.type == pygame.KEYDOWN and you_can_go_to_the_next_scene:
            going_to_the_next_scene = True
    
    # Logic
    screen.fill(WHITE)
    alpha += 0.4 if alpha < 20 else 1
    logo.set_alpha(alpha)
    if alpha > 255: you_can_go_to_the_next_scene = True
    screen.blit(logo, (450, 350))
    if you_can_go_to_the_next_scene and alpha % (FPS * 4) < FPS * 2:
        screen.blit(choplin.render("Press any key", True, BLACK), (450, 500))
    pygame.display.update()




