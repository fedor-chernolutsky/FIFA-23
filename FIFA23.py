# -*- coding: utf-8 -*-
import time
import ctypes
import pygame

# Screen resolution fix
ctypes.windll.user32.SetProcessDPIAware()

# Start PyGame
pygame.init()

screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

choplin = pygame.font.Font("Choplin-Medium.ttf", 32)
choplin_mini = pygame.font.Font("Choplin-Medium.ttf", 18)

logo = pygame.image.load("FIFA23.png")
splash = pygame.image.load("splash.png")
text = choplin.render('Press any button', True, BLACK)
text_mini = choplin_mini.render('This will be your default control device', True, BLACK)
screen_color = 0
alpha_logo = 0
alpha_splash = 0
alpha_text = 0
alpha_mini_text = 0
first = True
second = False
sunrise = True
you_can_go_to_the_next_screen = False

while True:
    clock.tick(FPS)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            quit()
        if event.type == pygame.KEYDOWN:
            print(pygame.mouse.get_pos())
    
    # Logic
    if first and sunrise:
        if screen_color < 253: screen_color += 2; alpha_logo += 2
        else: sunrise = False; time.sleep(2)
    elif first and not sunrise:
        if screen_color > 0: screen_color -= 2; alpha_logo -= 2
        else: first = False; second = True; sunrise = True

    if second: alpha_splash += 2
    you_can_go_to_the_next_screen = alpha_splash > 255
    alpha_text = alpha_splash % 500 if alpha_splash > 255 else 0

    screen.fill((screen_color, screen_color, screen_color))
    logo.set_alpha(alpha_logo)
    splash.set_alpha(alpha_splash)
    text.set_alpha(alpha_text)
    text_mini.set_alpha(alpha_text)
    screen.blit(logo, (550, 450))
    screen.blit(splash, (0, 0))
    screen.blit(text, (820, 780))
    screen.blit(text_mini, (780, 820))
    pygame.display.update()




