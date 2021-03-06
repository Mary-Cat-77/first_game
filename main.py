import pygame
pygame.init()
class Ball:
    def __init__ (self, poss, colour):
        self.poss = poss  # (100, 100)
        self.colour = colour
        pygame.draw.circle(screen, self.colour, self.poss, 50)

    def move(self):
        self.poss = (self.poss[0] + 1, self.poss[1])

    def renew(self):
        pygame.draw.circle(screen, self.colour, self.poss, 50)


screen = pygame.display.set_mode((600, 300))
clock = pygame.time.Clock()
n = (242, 138, 188)
first_ball = Ball((100, 100), n)
FPS = 100
x, y = 100, 100
flag = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            n = (245, 14, 126)
            pygame.draw.circle(screen, n, (x, y), 50)
    screen.fill((245, 14, 126))
    first_ball.move()
    pygame.draw.circle(screen, n, (x, y), 50)
    pygame.display.flip()

    if x + 50 == 600:
        flag = False
    elif x == 50 :
        flag = True
    if flag:
        x += 1
    else:
        x -= 1
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 50)
    clock.tick(FPS)
pygame.quit()