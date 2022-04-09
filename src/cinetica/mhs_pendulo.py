import math
import pygame
pygame.init()

theta = -1
while not ((theta >= 0) and (theta <= 10)):
    theta = float(input('Qual o angulo inicial em graus? (menor que 10) '))
m = float(input('Qual a massa do objeto? '))        # Por mero parâmetro experimental
L = float(input('Qual o comprimento da linha? (em m) '))

WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movimento Harmônico Simples")

WHITE = (210, 210, 210)
BLACK = (0, 0, 0, .8)

#FONT = pygame.font.SysFont("comicsans", 16)

class Objeto:
	g = 9.807 		       	                # Aceleração da gravidade (m/s^2)
	ESCALA = HEIGHT / L * 0.8	        # L == Altura da tela

	def __init__(self, angulo, m, L):
		self.angulo = theta
		self.A = L * math.sin(math.radians(angulo))
		self.x = 0
		self.y = 0
		self.m = m
		self.L = L
		self.diametro = 20
		self.movimento = []
		self.w = self.frequencia_angular()

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
		pygame.draw.lines(win, BLACK, False, [(WIDTH / 2 , 0) , (x, y)], 2)

	def transformacaoLinear(self, x, y):
		x += WIDTH / 2
		return x, y

	def frequencia_angular(self):
		L, g = self.L, self.g
		w = math.sqrt(g / L)
		return w

	def deslocamento(self, t):
		w, A, L = self.w, self.A, self.L
		x = w * A * math.cos(w*t)
		y = math.sqrt(math.pow(L, 2) - math.pow(x, 2))
		return x, y

	def update_position(self, t):
		self.x, self.y = self.deslocamento(t)
		x, y = self.transformacaoLinear(self.x * self.ESCALA, self.y * self.ESCALA)
		self.movimento.append((x, y))

def main(theta, m, L):
	run = True
	clock = pygame.time.Clock()
	t = 0
	objeto = Objeto(theta, m, L)

	while run:
		clock.tick(20)
		WIN.fill(WHITE)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		objeto.update_position(t)
		objeto.draw(WIN)

		pygame.display.update()

		t += 1/20
	pygame.quit()

main(theta, m, L)
