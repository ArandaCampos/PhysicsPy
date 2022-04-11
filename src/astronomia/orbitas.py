import pygame
import math
pygame.init()

distancia = float(input('Distancia entre o satélite e a terra em Km: '))
distancia *= math.pow(10, 3)

WIDTH, HEIGHT =  1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbitas de satélites")

BLACK = (0, 0, 0, 0.7)
WHITE = (255, 255, 255)
BLUE = (100, 149, 237)

RAIO_DA_TERRA = 12742000 / 2
#RAIO_DO_SATELITE = 100000 / 2
#FONT = pygame.font.SysFont("comicsans", 16)

proporcao = (1 / (distancia + RAIO_DA_TERRA)) * 0.9
escala_tela = (HEIGHT / 2) * proporcao 

class Corpo_celeste:
	G = 6.67428e-11
	ESCALA = HEIGHT / (distancia + RAIO_DA_TERRA)

	def __init__(self, x, y, raio, cor, massa):
		self.x = x
		self.y = y
		self.raio = raio
		self.cor = cor
		self.massa = massa
		
		self.R = x + RAIO_DA_TERRA
		self.g = 0
		self.v = 0
		self.theta = 0

		self.orbita = []
		self.planeta = False

	def desenhar(self, win, escala):
		x = self.x * escala + WIDTH / 2
		y = self.y * escala + HEIGHT / 2

		if len(self.orbita) > 2:
			atualizar_pontos = []
			for pontos in self.orbita:
				x, y = pontos
				x = x * escala + WIDTH / 2
				y = y * escala + HEIGHT / 2
				atualizar_pontos.append((x, y))

			pygame.draw.lines(win, self.cor, False, atualizar_pontos, 2)

		pygame.draw.circle(win, self.cor, (x, y), self.raio)

	def gravidade(self, terra):
		R, M = self.R, terra.massa
		g = self.G * M / math.pow(R, 2)
		return g

	def velocidade(self):
		R, g = self.R, self.g
		v = math.sqrt(R * g)
		T = 2 * 3.1415  * R / v 
		theta = 2 * 3.1415 / T
		return theta, v

	def posicao_angular(self, t):
		w = self.theta
		posicao_angular = w * t
		return posicao_angular

	def deslocamento(self, t):
		theta = self.posicao_angular(t)
		r = self.R
		x = r * math.sin(theta)
		y = r * math.cos(theta)
		return x, y

	def atualizar_posicao(self, t):
		x, y = self.deslocamento(t)
		self.orbita.append((x, y))


def main():
	run = True
	clock = pygame.time.Clock()

	terra = Corpo_celeste(0, 0, RAIO_DA_TERRA * escala_tela, BLUE, 5.9742 * 10**24)
	terra.planeta = True

	satelite = Corpo_celeste(distancia, 0, 4, WHITE, 0)
	satelite.g = satelite.gravidade(terra)
	satelite.theta, satelite.v = satelite.velocidade()
	
	t = 0
	while run:
		clock.tick(60)
		WIN.fill((0, 0, 0))
		t += 3600 				# t += 1 hora
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		
		tempo = t / (3600 * 24) 		# em dias
		print('Tempos %.1f em dias' %(tempo))
		satelite.atualizar_posicao(t)
		satelite.desenhar(WIN, escala_tela)
		
		terra.desenhar(WIN, escala_tela)

		pygame.display.update()

	pygame.quit()

main()