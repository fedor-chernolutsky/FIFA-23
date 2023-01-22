# -*- coding: utf-8 -*-
import ctypes
import pygame

from variables import FULL_HD
from splash_page import SplashPage
from menu_page import MenuPage

class FIFA23:
    def __init__(self):
        self.screen = pygame.display.set_mode(FULL_HD)
        self.clock = pygame.time.Clock()
        
        self.splash_page = SplashPage(self.clock, self.screen)
        self.menu_page = MenuPage(self.clock, self.screen)

        self.pages = {"splash_page": self.splash_page, "menu_page": self.menu_page}
        self.page = self.menu_page
    
    def change_page(self, page):
        self.page = page

    def launch(self):
        while True:
            self.change_page(self.page.run(self.pages))

if __name__ == "__main__":
    # Resolution fix
    ctypes.windll.user32.SetProcessDPIAware()
    # Start PyGame
    pygame.init()
    # Launch FIFA23
    FIFA23().launch()
