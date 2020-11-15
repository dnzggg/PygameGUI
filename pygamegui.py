import pygame

pygame.init()

class Frame:
    def __init__(self, w=500, h=500):
        self.w = w
        self.h = h
        self.screen = pygame.display((w, h))
