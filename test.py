import pygame, sys



screen = pygame.display.set_mode((640,480))

red = (255,0,0)

color = red

x = 100
y = 100

width = 400
height = 300


pygame.draw.rect(screen, color,(x,y,width,height))

pygame.display.update()
	