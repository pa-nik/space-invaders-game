import js as p5
from sprite import *
from spaceship import *
from bullet import *
from invader import *

print('10.1 space invaders (version 2)\n')

print('click on canvas and press arrow keys')
print('to move the ship, press space bar to')
print('shoot the invaders...')

# create (instantiate) the Spaceship object:
spaceship = Spaceship()  
# instantiate the Bullet object with x, y:
bullet = Bullet(x = 150, y = 0)  

# an empty list for invader objects:
invader_list = []  
for i in range(3):
  # instantiate Invader object (1st row):
  invader = Invader(x = 50 + i*100, y = 100)  
  # add invader to invader_list:
  invader_list.append(invader)  
  # instantiate Invader object (2nd row):
  invader = Invader(x = 50 + i*100, y = 25)  
  # add invader to invader_list:
  invader_list.append(invader) 

font = p5.loadFont('data/PressStart2P.otf')
shoot_sound = p5.loadSound('data/shoot.wav')

program_state = 'START'

def setup():
  p5.createCanvas(300, 300)  
  p5.rectMode(p5.CENTER)
  p5.imageMode(p5.CENTER)
  p5.textFont(font)
  p5.textSize(18)

def draw():
  global spaceship
  p5.background(0)    
  global program_state
  if(program_state == 'START'):
    p5.fill(255)
    p5.text('Click to Start..', 10, 150)
  if(program_state == 'PLAY'):
    bullet.update() 
    bullet.draw() 
    spaceship.draw()
    if(p5.keyIsPressed == True):
      if(p5.keyCode == p5.RIGHT_ARROW):
        if(spaceship.x < p5.width - 50):
          spaceship.x += 2
      elif(p5.keyCode == p5.LEFT_ARROW):
        if(spaceship.x > 50):
          spaceship.x -= 2 

    # use while loop to traverse invader_list
    # to delete invaders without error:
    i = 0  # loop counter variable
    while(i < len(invader_list)):
      invader = invader_list[i]
      invader.update()
      invader.draw()

      # distance between invader and bullet:
      d = p5.dist(invader.x, invader.y, 
                  bullet.x, bullet.y)
      if(d < 20):  
        print('invader hit!')
        # get rid of bullet:
        bullet.y = 0
        # remove invader i from invader_list:
        invader_list.pop(i)
        # win if invader_list becomes empty:
        if(len(invader_list) == 0):
          program_state = 'WIN'
      # check if the invader reached the bottom:
      if(invader.y > p5.height - 50):
          program_state = 'LOOSE'
      i += 1  # increment while loop counter
  elif(program_state == 'WIN'):
    p5.fill(255)
    p5.text('You Win!', 80, 150)
  elif(program_state == 'LOOSE'):
    p5.fill(255)
    p5.text('You Lose!', 60, 150)

def keyReleased(event):
  global bullet
  if(p5.key == ' '):
    # reset the bullet to spaceship coordinates:
    bullet.x = spaceship.x
    bullet.y = spaceship.y
    # play sound:
    shoot_sound.play()

def mousePressed(event):
  global program_state
  if(program_state == 'START'):
    program_state = 'PLAY'
    print('program_state = ' + program_state)
