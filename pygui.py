import pygame


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
        func.update(event)


class Slider:
    def __init__(self, screen, pos=(100, 100), line_color=(120, 120, 120), ellipse_color=(66, 134, 244), number=0,
                 range=10):
        self.screen = screen
        self.range = range
        self.number = number
        self.pressed = False
        self.line_b_color = line_color
        self.ellipse = None
        self.ellipse_color = self.line_a_color = ellipse_color
        self.y = pos[1]
        self.start_pos = self.start_a = pos
        self.end_pos = self.end_b = (pos[0] + 300, self.y)
        self.x = (pos[0] + self.end_pos[0]) / 2
        self.ellipse_pos = (self.x, self.y - 15, 10, 30)
        self.end_a = self.start_b = (self.x, self.y)
        self.draw()

    def update(self, event):
        x = self.ellipse_pos[0]
        y = self.ellipse_pos[1]
        height = self.ellipse_pos[3]
        width = self.ellipse_pos[2]
        mouse = pygame.mouse.get_pos()
        if x < mouse[0] < x + width and y < mouse[1] < y + height:
            self.ellipse_color = (255, 255, 255)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pressed = True
        else:
            self.ellipse_color = (66, 134, 244)
        if event.type == pygame.MOUSEBUTTONUP:
            self.pressed = False
        if self.pressed:
            if self.start_pos[0] - 5 < mouse[0] < self.end_pos[0]:
                self.x = mouse[0]
                self.end_a = (self.x, self.y)
                self.ellipse_pos = (self.x, self.y - 15, 10, 30)
                self.start_b = (self.x, self.y)
                self.number = (self.x - self.start_pos[0]) / (300 / self.range) + 1

    def draw(self):
        pygame.draw.line(self.screen, self.line_a_color, self.start_a, self.end_a, 2)
        pygame.draw.line(self.screen, self.line_b_color, self.start_b, self.end_b, 2)
        self.ellipse = pygame.draw.ellipse(self.screen, self.ellipse_color, self.ellipse_pos)


class RadioButton:
    def __init__(self, screen, pos=(500, 500), color=(125, 135, 175), active_color=(0, 255, 0), set=False):
        self.screen = screen
        self.color = color
        self.set = set
        self.active_color = self.c = active_color
        self.pos = pos
        self.pressed = False

    def update(self, event):
        self.active_color = (0, 0, 0)
        x = self.pos[0] - 12
        y = self.pos[1] - 12
        height = width = 24
        mouse = pygame.mouse.get_pos()
        if x < mouse[0] < x + width and y < mouse[1] < y + height:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.activate()
                self.pressed = True
        else:
            self.pressed = False
        if self.set:
            self.active_color = self.c

    def activate(self):
        self.set = True

    def deactivate(self):
        self.set = False

    def draw(self):
        pygame.draw.circle(self.screen, self.active_color, self.pos, 11)
        pygame.draw.circle(self.screen, self.color, self.pos, 12, 2)


class GetFunctionKey:
    def __init__(self, screen, key="g", pos=(200, 200), width=120, height=35, functonality="game"):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.height = height
        self.pressed = False
        self.functionality = functonality
        self.key = key.capitalize()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 20)
        self.text1 = self.myfont.render(self.key, True, (255, 0, 0))
        self.changed = False

    def update(self, event):
        if self.pressed:
            if pygame.mouse.get_pressed()[0] == 1:
                self.key = "Mb left"
                self.pressed = False
                self.changed = True
            elif pygame.mouse.get_pressed()[1] == 1:
                self.key = "Mb middle"
                self.pressed = False
                self.changed = True
            elif pygame.mouse.get_pressed()[2] == 1:
                self.key = "Mb right"
                self.pressed = False
                self.changed = True
            else:
                try:
                    self.key = pygame.key.name(list(pygame.key.get_pressed()).index(1))
                    self.pressed = False
                    self.changed = True
                except:
                    pass
            self.text1 = self.myfont.render(self.key.capitalize(), True, (255, 0, 0))
        if not self.changed:
            x = self.pos[0]
            y = self.pos[1]
            mouse = pygame.mouse.get_pos()
            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pressed = True
        self.changed = False

    def draw(self):
        self.screen.blit(self.text1, self.pos)
        x, y = self.pos[0], self.pos[1]
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x - 8, y - 3, self.width, self.height), 2)
        if self.pressed:
            w, h = pygame.display.get_surface().get_size()
            pygame.draw.rect(self.screen, (150, 150, 150), pygame.Rect((w / 2) - 90, (h / 2) - 45, 180, 90))
            text2 = self.myfont.render('Enter a key to', True, (0, 0, 0))
            text3 = self.myfont.render(self.functionality, True, (0, 0, 0))
            self.screen.blit(text2, ((w / 2) - 70, (h / 2) - 35))
            move = (25 * len(self.functionality)) / 4
            self.screen.blit(text3, ((w / 2) - move, (h / 2)))


pygame.init()
window = pygame.display.set_mode((800, 800))
func = GetFunctionKey(window)

while True:
    lookforinput()
    window.fill((0, 0, 0))
    func.draw()
    pygame.display.flip()
