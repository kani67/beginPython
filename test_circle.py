#test_circle.py
# this program fills the rectangle with red

import pygame, sys

screen = pygame.display.set_mode((600,600))

red = (255,0,0)

color = red

x = 300
y = 300

width = 400
height = 400
thickness = 2

radius = 200


while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit();sys.exit

	
	#pygame.draw.rect(screen, color,(x,y,width,height), thickness)
	
	#change rect to circle, remove width, height and add radius

	pygame.draw.circle(screen, color, (x,y), radius, thickness)
	
	

	pygame.display.update()		
