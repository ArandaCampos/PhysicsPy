from wsgiref.simple_server import WSGIRequestHandler
import pygame
import math
pygame.init()

x = float(input('Qual posição inicial em metros? '))
pf = float(input('Qual a posição final em metros '))
velocidade = float(input('Qual a velocidade inicial (m/s): '))
aceleracao = float(input('Qual a aceleracao, em m/s, do objeto? '))

WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movimento Retilíneo Uniformemente Variado")

WHITE = (210, 210, 210)
BLACK = (0, 0, 0, .8)

#FONT = pygame.font.SysFont("comicsans", 16)

class Objeto:
	g = -9.807 		       	# Aceleração da gravidade (m/s^2)
	P0 = x
	ESCALA = (WIDTH - 50) / (pf - x)				# 10px == 1 metro

	def __init__(self, x, velocidade, aceleracao, pf):
		self.x = x													# Posição Vertical (m)
		self.y = 2											# Posição Horizontal (m)
		self.pf = pf
		self.v = velocidade
		self.a = aceleracao
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

	def transformacaoLinear(self, x):
		x -= self.P0
		return x

	def velocidade(self, t):
		a, v = self.a, self.v
		V = v * t + (math.pow(t, 2) * a) / 2
		return V

	def deslocamento(self, t):
		v = self.velocidade(t)
		x = self.x
		px = x + v
		return px, v

	def update_position(self, t):
		x, v = self.deslocamento(t)
		y, pf = self.y, self.pf
		if x <= pf:
			print("%.2f | %.2f | %.2f" %(x, t, v))
			x = self.transformacaoLinear(x)
			self.movimento.append((x * self.ESCALA + 25 , HEIGHT - y * self.ESCALA - self.diametro))

def main(x, velocidade, aceleracao, p0):
	run = True
	clock = pygame.time.Clock()
	t = 0
	objeto = Objeto(x, velocidade, aceleracao, pf)

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

main(x, velocidade, aceleracao, pf)
