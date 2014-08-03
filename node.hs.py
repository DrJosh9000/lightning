import pygame
from pygame import display, draw, event, time
from random import choice, random, vonmisesvariate
from math import atan2, cos, pi, sin
pygame.init()
clock = time.Clock()
size = width, height = 1024, 768
start = width/2, 0
black = 0, 0, 0
white = 255, 255, 255
screen = display.set_mode(size)
step=5.0
kappa=2.0
fork=0.01
class Lightning():
	def __init__(self):
		self.paths = [[start]]
	def more(self):
		for p in self.paths:
			a = p[-1]
			if a[0] < 0 or a[0] > width or a[1] < 0 or a[1] > height:
				continue
			if len(p) < 2 or a[1] < 100:
				mu = pi / 2.0
			else:
				b = start
				mu = atan2(a[1]-b[1], a[0]-b[0])
				while mu < 0.0:
					mu += 2.0*pi
			t = vonmisesvariate(mu, kappa)
			dx, dy = step*cos(t), step*sin(t)
			p.append((a[0]+dx, a[1]+dy))
		if random() < fork:
			self.paths.append([choice(self.paths)[-1]])
	def draw(self):
		for p in self.paths:
			a = p[0]
			for b in p[1:]:
				draw.line(screen, white, a, b, 3)
				a = b
done = False
lightning = Lightning()
while not done:
	clock.tick(60)
	for ev in event.get():
		if ev.type == pygame.QUIT:
			done = True
			break
		if ev.type == pygame.KEYDOWN:
			if ev.key in (pygame.K_ESCAPE, pygame.K_q):
				done = True
			elif ev.key == pygame.K_r:
				lightning = Lightning()
	for i in xrange(100):
		lightning.more()
	screen.fill(black)
	lightning.draw()
	display.flip()
pygame.quit()