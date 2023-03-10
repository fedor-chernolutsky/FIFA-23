# -*- coding: utf-8 -*-
import time
import pygame
from variables import BLACK, WHITE, FPS

class SplashPage:
    
    def __init__(self, screen):
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.choplin = pygame.font.Font("Choplin-Medium.ttf", 32)
        self.choplin_mini = pygame.font.Font("Choplin-Medium.ttf", 18)

        self.logo = pygame.image.load("FIFA23.png")
        self.splash = pygame.image.load("splash.png")
        self.text = self.choplin.render('Press any button', True, BLACK)
        self.text_mini = self.choplin_mini.render('This will be your default control device', True, BLACK)

        self.screen_color = 0
        self.alpha_logo = 0
        self.alpha_splash = 0
        self.alpha_text = 0
        self.alpha_mini_text = 0
        self.first = True
        self.second = False
        self.sunrise = True
        self.you_can_go_to_the_next_screen = False
        self.going_to_the_next_screen = False
    
    def run(self):
        while True:
            self.clock.tick(FPS)
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    quit()

                if self.you_can_go_to_the_next_screen and event.type == pygame.KEYDOWN:
                    self.going_to_the_next_screen = True
                    self.second = False; self.alpha_splash = 255
            
            # Logic
            if self.first and self.sunrise:
                if self.screen_color < 253: self.screen_color += 2; self.alpha_logo += 2
                else: self.sunrise = False; time.sleep(2)
            elif self.first and not self.sunrise:
                if self.screen_color > 0: self.screen_color -= 2; self.alpha_logo -= 2
                else: self.first = False; self.second = True; self.sunrise = True

            if self.second: self.alpha_splash += 2
            self.you_can_go_to_the_next_screen = self.alpha_splash > 255
            self.alpha_text = self.alpha_splash % 500 if self.alpha_splash > 255 else 0
            
            if self.going_to_the_next_screen: self.alpha_splash -= 2
            
            if self.alpha_splash < 0: return "menu_page"


            self.screen.fill((self.screen_color, self.screen_color, self.screen_color))
            self.logo.set_alpha(self.alpha_logo)
            self.splash.set_alpha(self.alpha_splash)
            self.text.set_alpha(self.alpha_text)
            self.text_mini.set_alpha(self.alpha_text)
            self.screen.blit(self.logo, (550, 450))
            self.screen.blit(self.splash, (0, 0))
            self.screen.blit(self.text, (820, 780))
            self.screen.blit(self.text_mini, (780, 820))
            pygame.display.update()
