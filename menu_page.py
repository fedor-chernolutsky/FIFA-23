# -*- coding: utf-8 -*-
import pygame
from page import Page
from variables import BLACK, WHITE

class MenuPage(Page):

    def initialize(self):
        self.GRASS_COLOR = (173, 206, 129)
        self.logo = pygame.transform.scale(pygame.image.load("FIFA23.png"), (256, 60))    
        white = pygame.Surface((256, 60)); white.fill(WHITE)
        self.logo.blit(white, (0, 0), special_flags=pygame.BLENDMODE_BLEND)

    def eventually(self, event):
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: quit()

    def refresh(self):
        pass

    def render(self):
        self.screen.fill(self.GRASS_COLOR)
        self.screen.blit(self.logo, (10, 10))
