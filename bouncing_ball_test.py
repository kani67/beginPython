# Bouncing ball
# Demonstrates dealing with screen boundaries

import pygame, sys

pygame.init()

width = 640
height = 480
radius = 20

red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
color = red
thickness = 2


screen = pygame.display.set_mode((width, height))

x = width / 2
y = height / 2


speed_x = 0.5
speed_y = 1



pygame.draw.circle(screen, white, (int(x),int(y)), radius)

while True:
  

  screen.fill(black)

  pygame.draw.circle(screen, color, (int(x),int(y)), radius)
  
  
  
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN: 
      if event.key == pygame.K_ESCAPE: 
        pygame.quit();sys.exit() 
    if event.type == pygame.QUIT:
        pygame.quit();sys.exit()

  
  x += speed_x
  y += speed_y
  
  
  #reversing velocity
  # by taking speed * -1

  if x < 0:
    x = 20
    speed_x *= -1
 
  if x > width - radius:
    x = width - radius
    speed_x *= -1

  if y < 0:
    y = 20
    speed_y *= -1

  if y > height - radius:
    y = height - radius
    speed_y *= -1    

  pygame.display.update() 