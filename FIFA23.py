# -*- coding: utf-8 -*-
import ctypes
import pygame

from variables import FULL_HD, FPS
from splash_page import SplashPage
from menu_page import MenuPage

class FIFA23:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(FULL_HD)

        self.splash_page = SplashPage(self.screen)
        self.menu_page = MenuPage(self.screen)

        self.pages = {"splash_page": self.splash_page, "menu_page": self.menu_page}
        self.page = self.menu_page
    
    def change_page(self, name):
        if name is None: pass
        else: self.page = self.pages[name]

    def launch(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get(): self.page.eventually(event)
            self.change_page(self.page.refresh())
            self.page.render()
            pygame.display.update()


if __name__ == "__main__":
    # Resolution fix
    ctypes.windll.user32.SetProcessDPIAware()
    # Start PyGame
    pygame.init()
    # Launch FIFA23
    FIFA23().launch()
