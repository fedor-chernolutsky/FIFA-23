# -*- coding: utf-8 -*-
import pygame

class Page:
    def __init__(self, screen):
        self.screen = screen
        self.initialize()

    def initialize(self): pass
    def eventually(self, event): pass
    def refresh(self): pass
    def render(self): pass