import js as p5

# class definition for the Spaceship object:
class Spaceship():  
  x = 150
  y = 282

  def __init__(self):
    self.img = p5.loadImage(
      'data/spaceship.png')

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0)
    p5.pop()