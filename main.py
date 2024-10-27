import pygame
import sys
import random
import math

width = 1000
height = 500

G = 1

def	norm(a, b):
	return math.sqrt(abs(a.x - b.x) ** 2 + abs(a.y - b.y) ** 2)

class	particle:
	def	__init__(self, x, y, radius, color):
		self.x = x
		self.y = y
		self.speed_x = 0
		self.speed_y = 0
		self.radius = radius
		self.color = color
		self.ax = 0
		self.ay = 0

	def	move(self, dots):
		for dot in dots:
			r = norm(self, dot)
			if r == 0:
				continue
			F = G / r ** 2
			fx = F * (dot.x - self.x) / r
			fy = F * (dot.y - self.y) / r
			self.ax += fx
			self.ay += fy
			dot.ax -= fx
			dot.ay -= fy

		self.speed_x += self.ax
		self.speed_y += self.ay
		dot.speed_x += dot.ax
		dot.speed_y += dot.ay
		self.x += self.speed_x
		self.y += self.speed_y
		dot.x += dot.speed_x
		dot.y += dot.speed_y
		if self.x < 0:
			self.x = width
		if self.x > width:
			self.x = 0
		if self.y < 0:
			self.y = height
		if self.y > height:
			self.y = 0
		self.ax = 0
		self.ay = 0

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

	dots = [particle(random.randint(0, width), random.randint(0, height), 2, 0xFFF50A4) for _ in range(100)]
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
	
		screen.fill(0x0A022B)
		i = 0
		for i in range(len(dots)):
			dots[i].draw(screen)
			dots[i].move(dots)
			dots[i].speed_y -= 1
			dots[i].speed_x -= 1
		#keys = pygame.key.get_pressed()
		#dots[0].dep(keys)
		#dots[0].draw(screen)
		pygame.display.flip()
		pygame.time.Clock().tick(60)

	pygame.quit()
	sys.exit()

if __name__ == "__main__":
	main()
