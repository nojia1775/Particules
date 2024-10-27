import pygame
import sys
import random
import math

width = 1000
height = 500

G = 0.1

def	norm(ax, ay, bx, by):
	return math.sqrt(abs(ax - bx)**2 + abs(ay - by)**2)

class	particle:
	def	__init__(self, x, y, radius, color):
		self.x = x
		self.y = y
		self.velocity_x = 0
		self.velocity_y = 0
		self.radius = radius
		self.color = color

	def	move(self, dots, surface):
		tmp_x = 0
		tmp_y = 0
		for dot in dots:
			if norm(self.x, self.y, dot.x, dot.y) == 0:
				tmp_x += 0
			else:
				tmp_x += 1 / norm(self.x, self.y, dot.x, dot.y) * (self.x - dot.x)
			if norm(self.x, self.y, dot.x, dot.y) == 0:
				tmp_y = 0
			else:
				tmp_y += 1 / norm(self.x, self.y, dot.x, dot.y) * (self.y - dot.y)
		pygame.draw.line(surface, 0xFFFFFF, (self.x, self.y), (tmp_x, tmp_y))

		if self.x < 0:
			self.x = width
		if self.x > width:
			self.x = 0
		if self.y < 0:
			self.y = height
		if self.y > height:
			self.y = 0

	def	dep(self, keys):
		if keys[pygame.K_UP]:
			self.y -= 5
		if keys[pygame.K_DOWN]:
			self.y += 5
		if keys[pygame.K_LEFT]:
			self.x -= 5
		if keys[pygame.K_RIGHT]:
			self.x += 5

	def	draw(self, surface):
		pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

		
def	main():
	pygame.init()

	screen = pygame.display.set_mode((width, height))

	dots = [particle(random.randint(0, width / 2) + width / 2, random.randint(0, height / 2) + height / 2, 5, 0xF00000) for _ in range(2)]
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
	
		screen.fill(0x0A022B)
		i = 0
		for i in range(2):
			dots[i].draw(screen)
			dots[i].move(dots, screen)
		keys = pygame.key.get_pressed()
		dots[0].dep(keys)
		dots[0].draw(screen)
		pygame.display.flip()
		pygame.time.Clock().tick(60)

	pygame.quit()
	sys.exit()

if __name__ == "__main__":
	main()