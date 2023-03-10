# -*- coding: utf-8 -*-
import pygame
from variables import BLACK, WHITE, FPS

class MenuPage:
    
    def __init__(self, screen):
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.GRASS_COLOR = (173, 206, 129)
        
        self.logo = pygame.transform.scale(pygame.image.load("FIFA23.png"), (256, 60))    
        white = pygame.Surface((256, 60)); white.fill(WHITE)
        self.logo.blit(white, (0, 0), special_flags=pygame.BLENDMODE_BLEND)
    
    def run(self):

        while True:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    quit()
            
            self.screen.fill(self.GRASS_COLOR)
            self.screen.blit(self.logo, (10, 10))
            pygame.display.update()