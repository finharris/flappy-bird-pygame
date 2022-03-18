import pygame
import random

size = 940, 640
width, height = size

# colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

pygame.init()

clock = pygame.time.Clock()

background = CYAN

screen = pygame.display.set_mode(size)

bird = pygame.image.load('bird.png')
bird = pygame.transform.smoothscale(bird, (50,50))
bird_y = height/2
bird_x = width/5
bird_rect = bird.get_rect()
bird_velocity = 0
bird_acceleration = 0.009
bird_max_up_velocity = -0.4
bird_jump_velocity = 0.4

class Pipe:
  x = width
  y = random.randint(70, height-70)
  image = pygame.image.load('pipe.png')
  mask = pygame.mask.from_surface(image)
  bounding_rects = mask.get_bounding_rects()
  rect = image.get_rect()
  speed = 2
  
  def __init__(self):
    self.rect.center = (self.x, self.y)
  
  def destroy(self):
    print('gone')
  
  def setx(self, new_x):
    self.x = new_x
    self.rect.center = (new_x, self.y)

pipe1 = Pipe()

pipes = [pipe1]

# event loop
running = True
while running:
  dt = clock.tick(60)
  
  for event in pygame.event.get():
    # quit on quit button press
    if event.type == pygame.QUIT:
      running = False
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        bird_velocity = max(bird_velocity-bird_jump_velocity, bird_max_up_velocity)
        
  bird_velocity += bird_acceleration
  bird_y += bird_velocity * dt
  
  bird_rect.center = (bird_x, bird_y)
  
  if bird_rect.midtop[1] < 0 or bird_rect.midbottom[1] > height:
    print('fail')
    running = False
  
  # pipes
  for pipe in pipes:
    if pipe.x < 0:
      pipe.destroy()
    
    pipe.setx(pipe.x - pipe.speed)
    
  # check if bird is in pipe collide
  
      
  # render stuff
  screen.fill(background)
  screen.blit(bird, bird_rect)
  
  for pipe in pipes:
    screen.blit(pipe.image, pipe.rect)
  
    
  # render the screen
  pygame.display.update()


pygame.quit()