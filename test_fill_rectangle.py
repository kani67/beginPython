#test_fill_rectangle.py
# this program fills the rectangle with red

import pygame, sys

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

	
	#remove thickness and the rectangle will be filled in with red
	#pygame.draw.rect(screen, color,(x,y,width,height), thickness)
	pygame.draw.rect(screen, color,(x,y,width,height))
	

	pygame.display.update()		
