import pygame
from pygame import *


def lookforinput():
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
            if event.key == pygame.K_ESCAPE:
                pass
            elif event.key == pygame.K_F4 and alt_pressed:
                exit()
        ib.handle_events(event)


class InputBox:
    def __init__(self, screen, x, y, w, h, text=""):
        self.screen = screen
        self.w = w
        self.rect = Rect(x, y, w, h)
        self.active_color = (28, 134, 238)
        self.inactive_color = (141, 182, 205)
        self.color = self.inactive_color
        self.text = text
        self.active = False
        self.font = font.SysFont('Comic Sans MS', 20)
        self.text1 = self.font.render(self.text, True, (255, 255, 255))

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos[0], event.pos[1]):
                self.active = True
            else:
                self.active = False
            self.color = self.active_color if self.active else self.inactive_color
        if event.type == KEYDOWN:
            if self.active:
                if event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key in [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]:
                    self.text += event.unicode
                self.text1 = self.font.render(self.text, True, (255, 255, 255))

    def draw(self):
        self.screen.blit(self.text1, (self.rect.x+5, self.rect.y+5))
        draw.rect(self.screen, self.color, self.rect, 2)

    def update(self):
        width = max(self.w, self.text1.get_width()+10)
        self.rect.w = width


pygame.init()
window = pygame.display.set_mode((800, 800))
ib = InputBox(window, 100, 100, 140, 40)

while True:
    lookforinput()
    window.fill((30, 30, 30))
    ib.update()
    ib.draw()
    pygame.display.flip()
