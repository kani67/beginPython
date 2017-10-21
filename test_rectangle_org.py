#test_rectangle.py

import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640,480))

red = (255,0,0)

color = red

x = 100
y = 100

width = 400
height = 300
thickness = 2

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit();sys.exit

	pygame.draw.rect(screen, color, (x,y,width,height), thickness)

	pygame.display.update()