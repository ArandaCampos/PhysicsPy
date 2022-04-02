import pygame

HEIGHT, WIDTH = 600, 1200
x = float(input('Qual a posição inicial do objeto? (metros) '))
pf = float(input('Qual a posição final do objeto? (metros) '))
v = float(input('Qual a velocidade do objeto? (km/h) '))

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Movimento Uniforme')

WHITE = (210, 210, 210)
BLACK = (0, 0, 0, 0.8)

FONT = pygame.font.SysFont("comicsans", 16)

class Objeto:
    ESCALA = 10
    def __init__ (self, x, pf, v):
        self.x = x
        self.pf = pf
        self.v = v
        self.diametro = 20
        self.movimento = []

    def draw(self, win):
        updated_points = []
        for point in self.movimento:
            x, y = point
            x = x
            y = y
            updated_points.append((x, y))

        if len(self.movimento) > 2:
            pygame.draw.lines(win, BLACK, False, updated_points, 2)

        pygame.draw.circle(win, BLACK, (x, y), self.diametro)

    def deslocamento(self, t):
        vk = self.v
        v = vk / 3.6
        x = self.x
        px = x + v * t
        return px, v

    def update_position(self, t):
        x, v = self.deslocamento(t)
        pf, diametro = self.pf, self.diametro
        if x <= pf:
            print("%.2f | %.2f | %.2f" %(x, t, v))
            self.movimento.append((x * self.ESCALA + diametro , HEIGHT - 1.1 * diametro))

def main(x, pf, v):
    run = True
    clock = pygame.time.Clock()
    t = 0
    objeto = Objeto(x, pf, v)

    while run:
        clock.tick(20)
        WIN.fill(WHITE)
        t += 1/20

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        objeto.update_position(t)
        objeto.draw(WIN)

        pygame.display.update()

    pygame.quit()
    run = True

main(x, pf, v)

