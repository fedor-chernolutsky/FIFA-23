# -*- coding: utf-8 -*-
import pygame
from variables import BLACK, WHITE, FPS

class MenuPage:
    
    def __init__(self, clock, screen):
        self.clock = clock
        self.screen = screen
        self.grass_color = (173, 206, 129)
        
        self.logo = pygame.transform.scale(pygame.image.load("FIFA23.png"), (256, 60))
        self.white = pygame.Surface((256, 60))
        self.white.fill(WHITE)
        self.logo.blit(self.white, (0, 0), special_flags=pygame.BLENDMODE_BLEND)
        
    
    def run(self, pages):

        while True:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    quit()
            
            self.screen.fill(self.grass_color)
            self.screen.blit(self.logo, (10, 10))
            pygame.display.update()