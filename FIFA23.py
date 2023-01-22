# -*- coding: utf-8 -*-
# Resolution fix
import ctypes
ctypes.windll.user32.SetProcessDPIAware()
# Start PyGame
import pygame
pygame.init()

from variables import FULL_HD
from splash_page import SplashPage
from menu_page import MenuPage

screen = pygame.display.set_mode(FULL_HD)
clock = pygame.time.Clock()

splash_page = SplashPage(clock, screen)
menu_page = MenuPage(clock, screen)

pages = {"splash_page": splash_page, "menu_page": menu_page}

page = splash_page

while True:
    page = page.run(pages)




