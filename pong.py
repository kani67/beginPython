# Bouncing Ball
# Demonstrates dealing with screen boundaries

from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50) 



class Paddle(games.Sprite):
    """
    A paddle controlled by player to avoid falling drops.
    """
    image = games.load_image("pong_red_paddle.jpg")

    def __init__(self):
        """ Initialize Paddle object and create Text object for score. """
        super(Paddle, self).__init__(image = Paddle.image,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)
        
        self.score = games.Text(value = 100, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)
        
        self.time_til_drop = 0

    def update(self):
        """ Move to mouse x position. """
        self.x = games.mouse.x
        
        if self.left < 0:
            self.left = 0
            
        if self.right > games.screen.width:
            self.right = games.screen.width
            
        self.check_catch()    
                           
        
    def check_catch(self):
        """ Check if catch ball. """
        for ball in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10 
            Ball.handle_hits()
                
 
class Ball(games.Sprite):
    """ A bouncing ball. """
    
    speed = 3
    ball_image = games.load_image("pong_red_ball.jpg")
     
    def __init__(self):
        """ Initialize a Ball object. """
        super(Ball, self).__init__(image = Ball.image,
        dx = 1, dy = 1,
        dy = Ball.speed)
        
        games.screen.add(the_ball)
        
        
    
    def handle_hits(self):
        """ Destroy self if hit. """
        self.destroy()
        
    def update(self):
        """ Reverse a velocity component if edge of screen reached. """
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy
            
            

def main():
    """ Play the game. """
   
    
    the_paddle = Paddle()
    games.screen.add(the_paddle)
    
    x= 55
    
    the_ball = Ball()
    games.screen.add(the_ball)
    
    games.mouse.is_visible = False

    games.screen.event_grab = True
    games.screen.mainloop()

# start it up!
main()