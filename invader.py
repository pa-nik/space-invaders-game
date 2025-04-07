import js as p5
from sprite import *

# class definition for the Invader object
# as a child of Sprite object:
class Invader(Sprite):

  # overwrite the __init__ method of parent:
  def __init__(self, x = 150, y = 150):
    self.x = x  
    self.y = y
    self.timer = p5.millis()
    self.img1 = p5.loadImage('data/invader_1.png');  
    self.img2 = p5.loadImage('data/invader_2.png');   
      
  def update(self):
    # move it down every half a second:
    if(p5.millis() > self.timer + 500):
      self.y += 5
      # don't forget to update timer attribute:
      self.timer = p5.millis()  

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    # change image to display every half sec:
    if(p5.millis() % 1000 < 500):
      p5.image(self.img1, 0, 0)
    else:
      p5.image(self.img2, 0, 0)
    p5.pop()