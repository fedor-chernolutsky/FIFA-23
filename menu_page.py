# -*- coding: utf-8 -*-
import pygame
from variables import BLACK, WHITE, FPS

class MenuPage:
    
    def __init__(self, clock, screen):
        self.clock = clock
        self.screen = screen
    
    def run(self, pages):

        while True:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    quit()
            
            self.screen.fill(WHITE)
            pygame.display.update()