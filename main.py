# TODO: draw outlines, draw path
import math
import pygame

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (225, 225, 225)
RED = (200, 20, 20)
GREEN = (20, 200, 20)
BLUE = (20, 20, 200)

# Init prog
pygame.init()
size = (1280, 720)
center = [int(i) for i in (size[0] / 2, size[1] / 2)]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Orbit")
clock = pygame.time.Clock()
done = False

class Planet:
    def __init__(self, mass, orbit_len, angle, ang_speed, color):
        self.mass = mass
        self.orbit_len = orbit_len
        self.angle = angle
        self.ang_speed = ang_speed
        self.color = color

        # To update
        self.pos = (0, 0)
        self.crx = (0, 0)

    def update(self, crx):
        self.angle += self.ang_speed
        self.pos = [int(i) for i in (math.cos(self.angle) * self.orbit_len + crx[0], 
                                     math.sin(self.angle) * self.orbit_len + crx[1])]
        self.crx = crx

    def draw(self):
        pygame.draw.circle(screen, self.color, self.crx, self.orbit_len, 1)
        pygame.draw.circle(screen, self.color, self.pos, self.mass)

# Init
mass_center = 20
# 2d array of planets (first one is planet, following are moons)
planets = [[Planet(6, 100, 0, 0.06, GREEN), Planet(4, 80, 0, 0.1, BLUE), Planet(2, 20, 0, 0.11, RED)],
           [Planet(6, 200, 0, 0.05, GREEN), Planet(4, 80, 0, 0.1, BLUE)],
           [Planet(6, 300, 0, 0.04, GREEN), Planet(4, 80, 0, 0.1, BLUE)]]

# Text
text = pygame.font.SysFont("Gill Sans", 25)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    # draw and update
    screen.fill(GRAY)

    # outlines
#    pygame.draw.circle(screen, GREEN, center, orbit_l, 1)
#    pygame.draw.circle(screen, BLUE, pos_l, orbit_s, 1)

    for row in planets:
        for idx, col in enumerate(row):
            if idx == 0:
                col.update(center)
            else:
                col.update(row[0].pos)

            col.draw()

    # planets
    pygame.draw.circle(screen, RED, center, mass_center)

    pygame.display.flip()

    # 60 fps
    clock.tick(60)

pygame.quit()
