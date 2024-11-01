import pygame
import sys
import random
import math

BLEU = 0
JAUNE = 1
ROUGE = 2

nbr_particle = 200
width = 500
height = 500

G = 10000

"""
	_________________________
	 |bleu	|jaune	|vert	|
_________________________________
bleu	|deteste|aime	|deteste|
_________________________________
jaune	|null	|aime	|aime	|
_________________________________
vert	|deteste|aime	|null	|
_________________________________
"""

# plus c'est petit plus c'est le chaos (3 = mid)
chaos = 2
 
interaction = [
    [-1, 10, -1],
    [0, 1, 1],
    [-1, 1, 0]
]

colors = [0xFFF50A, 0xFFFF00]

colors = [
	[0x0000FF, BLEU],
	[0xFFFF00, JAUNE],
	[0xFF0000, ROUGE]
]

for i in range(len(interaction)):
	for j in range(len(interaction[i])):
		interaction[i][j]

class	particle:
	def	__init__(self, x, y, radius, color, type_part):
		self.x = x
		self.y = y
		self.speed_x = 0
		self.speed_y = 0
		self.radius = radius
		self.color = color
		self.type = type_part

	def	gravitation(self, dot):
		if self != dot:
			distance = math.sqrt((self.x - dot.x) ** 2 + (self.y - dot.y) ** 2)
			if distance != 0:
				force = interaction[self.type][dot.type] * G / (distance ** chaos)
				self.speed_x = force * ((dot.x - self.x) / distance)
				if self.speed_x > 0.5:
					self.speed_x = 0.5
				elif self.speed_x < -0.5:
					self.speed_x = -0.5
				self.speed_y = force * ((dot.y - self.y) / distance)
				if self.speed_y > 0.5:
					self.speed_y = 0.5
				elif self.speed_y < -0.5:
					self.speed_y = -0.5

	def	move(self):
		self.x += self.speed_x
		self.y += self.speed_y

		# frottement
		self.speed_y += -self.speed_y / 100
		self.speed_x += -self.speed_x / 100
		
		# fenetre infini
		if self.x < 0:
			self.x = width
		if self.x > width:
			self.x = 0
		if self.y < 0:
			self.y = height
		if self.y > height:
			self.y = 0

	def	control(self, keys):
		if self.x < 0:
			self.x = width
		if self.x > width:
			self.x = 0
		if self.y < 0:
			self.y = height
		if self.y > height:
			self.y = 0

		if keys[pygame.K_UP]:
			self.speed_y -= 5
		elif keys[pygame.K_DOWN]:
			self.speed_y += 5
		elif keys[pygame.K_LEFT]:
			self.speed_x -= 5
		elif keys[pygame.K_RIGHT]:
			self.speed_x += 5
		else:
			self.speed_x = 0
			self.speed_y = 0

	def	draw(self, surface):
		pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

	def	deal_collision(self, b):
		dx = self.x - b.x
		dy = self.y - b.y
		distance = math.hypot(dx, dy)
		if distance <= 0.01:
			return
		nx = dx / distance
		ny = dy / distance
		p = 2 * (self.speed_x * nx + self.speed_y * ny - b.speed_x * nx - b.speed_y * ny) / 2
		self.speed_x -= p * nx
		self.speed_y -= p * ny
		b.speed_x += p * nx
		b.speed_y += p * ny

		overlap = (self.radius + b.radius - distance) / 2
		self.x += overlap * nx
		self.y += overlap * ny
		b.x -= overlap * nx
		b.y -= overlap * ny

	def	detect_collision(self, b) -> bool:
		distance = math.hypot(self.x - b.x, self.y - b.y)
		return distance <= self.radius + b.radius + 1
		
def	main():
	pygame.init()

	screen = pygame.display.set_mode((width, height))

	dots = []
	for i in range(0, nbr_particle):
		dots.append(particle(random.randint(0, width), random.randint(0, height), 2, colors[i % 3][0], colors[i % 3][1]))

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
	
		screen.fill(0x0A021C)
		for i in range(len(dots)):
			for j in range(len(dots)):
				dots[i].gravitation(dots[j])
				dots[i].draw(screen)
				dots[i].move()
				if dots[i].detect_collision(dots[j]) and i != j:
					dots[i].deal_collision(dots[j])
		pygame.display.flip()
		#pygame.time.Clock().tick(1000)

	pygame.quit()
	sys.exit()
	sys.exit()

if __name__ == "__main__":
	main()