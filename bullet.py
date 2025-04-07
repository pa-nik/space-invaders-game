import js as p5
from sprite import *

# class definition for the Bullet object
# as a child of Sprite object:
class Bullet(Sprite):  
  
  # make it always animate upwards:
  def update(self):
    self.y -= 2
    
  def draw(self):
    p5.fill(255, 0, 127)
    p5.rect(self.x, self.y, 4, 8)
