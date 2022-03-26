import numpy as np
import pygame
import math
pygame.init()

WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MUV e MRU com projétil")

WHITE = (210, 210, 210)
BLACK = (0, 0, 0, .8)

FONT = pygame.font.SysFont("comicsans", 16)

class Objeto:
	g = -9.807 		       	# Aceleração da gravidade (m/s^2)
	ESCALA = 10				# 10px == 1 metro

	def __init__(self, x, y, velocidade, angulo, raio):
		self.x = x													# Posição Vertical (m)
		self.y = y													# Posição Horizontal (m)
		self.vy = velocidade * math.sin(math.radians(angulo))		# Velocidade Inicial eixo y
		self.vx = velocidade * math.cos(math.radians(angulo))		# Velocidade Inicial eixo x
		self.angulo = angulo
		self.raio = raio 			# Raio (m)
		self.orbita = []

	def draw(self, win):
		updated_points = []
		for point in self.orbita:
			x, y = point
			x = x
			y = y
			updated_points.append((x, y))

		if len(self.orbita) > 2:
			pygame.draw.lines(win, BLACK, False, updated_points, 2)

		pygame.draw.circle(win, BLACK, (x, y), self.raio)

	def velocidade(self, t):
		vx, vy, g = self.vx, self.vy, self.g
		Vx = vx * t
		Vy = vy * t + g * math.pow(t, 2) / 2
		return Vx, Vy

	def deslocamento(self, t):
		vx, vy = self.velocidade(t)
		x, y = self.x, self.y
		px = x + vx
		py = y + vy
		return px, py

	def update_position(self, t):
		x, y = self.deslocamento(t)
		if y >= 0:
			print(f'{x} | {y}')
			self.orbita.append((x * self.ESCALA , HEIGHT - y * self.ESCALA - self.raio))

def main():
	run = True
	clock = pygame.time.Clock()
	t = 0
	objeto = Objeto(0, 10, 30, 45, 20)

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

main()
