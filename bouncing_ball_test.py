# Bouncing ball
# Demonstrates dealing with screen boundaries

import pygame, sys

pygame.init()

width = 640
height = 480
radius = 20

red = (255,0,0)
black = (0,0,0)
color = red
thickness = 2


screen = pygame.display.set_mode((width, height))

x = 20
y = 20


speed = 0.005

vector = [x, y]


while True:
  

  screen.fill(black)

  pygame.draw.circle(screen, color, (int(x),int(y)), radius)


  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN: 
      if event.key == pygame.K_ESCAPE: 
        pygame.quit();sys.exit() 
    if event.type == pygame.QUIT:
        pygame.quit();sys.exit()

  
  x += vector[0] * speed
  y += vector[1] * speed
   
  if x > width: 
    x = width

  #if x < width:
   # x += x  
  
  if x < width:
    x += 0

  if y > height:
    y = height

  #if y < height:
   # y += y   

  if y < height:
    y = 0  

  pygame.display.update() 