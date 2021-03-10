import pygame
import random
pygame.init()
class Ball:
    def __init__ (self, poss, colour, radius):
        self.poss = poss  # (100, 100)
        self.colour = colour
        self.dir = list(random.choices(range(-4, 5), k=2))
        self.radius = radius
        pygame.draw.circle(screen, self.colour, self.poss, self.radius)

    def move(self):
        if self.poss[0] + self.radius == 1000:
            self.dir[0] *= -1
        elif self.poss[0] == self.radius:
            self.dir[1] *= -1
        if self.dir:
            self.poss = self.poss[0] - self.dir[0], self.poss[1]
        else:
            self.poss = self.poss[0] + self.dir[1], self.poss[1]
        self.poss = (self.poss[0], self.poss[1])

    def renew(self):
        pygame.draw.circle(screen, self.colour, self.poss, self.radius)

    def ball_intersaction(self, other):
        if ((self.poss[0] - other.poss[0]) ** 2) + ((self.poss[1] - other.poss[1]) ** 2) <= (self.radius + other.radius) ** 2:
            return True
        else:
            return False


balls = []
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
n = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
FPS = random.randint(50, 100)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                n = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                balls.append(Ball(event.pos, n, random.randint(1, 60)))
            elif event.button == 3:
                if len(balls) > 0:
                    n = (245, 14, 126)
                    pygame.draw.circle(screen, n, balls[0].poss, balls[0].radius)
                    del balls[0]
    screen.fill((245, 14, 126))
    for i in range(len(balls)):
        balls[i].move()
        balls[i].renew()
    i = 0
    while i < len(balls):
        j = i + 1
        while j < len(balls):
            if balls[i].ball_intersaction(balls[j]):
                balls.pop(j)
                balls.pop(i)
                break
            else:
                j += 1
        i += 1

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()