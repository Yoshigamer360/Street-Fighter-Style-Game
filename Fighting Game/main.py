# Started 4/11/24
# Made by Yoshi Gamer 360
import pygame
from fighter import Fighter

pygame.init()

# Create game window
screenWidth = 1000
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Brawler')

# set framerate
clock = pygame.time.Clock()
fps = 60

# define colours
red = (255, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)

# load background image
bgImage = pygame.image.load('assets/images/background/background.jpg').convert_alpha()

# function for drawing background
def drawBg():
    scaledBg = pygame.transform.scale(bgImage, (screenWidth, screenHeight))
    screen.blit(scaledBg, (0, 0))

# function for drawing healthbars
def drawHealthBar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, white, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, red, (x, y, 400, 30))
    pygame.draw.rect(screen, yellow, (x, y, 400*ratio, 30))

# create two instances of fighters
fighter1 = Fighter(200, 310)
fighter2 = Fighter(700, 310)

# Game loop
run = True
while run:

    clock.tick(fps)

    # draw background
    drawBg()

    # show player stats
    drawHealthBar(fighter1.health, 20, 20)
    drawHealthBar(fighter2.health, 580, 20)
    # move fighters
    fighter1.move(screenWidth, screenHeight, screen, fighter2)

    # draw fighters
    fighter1.draw(screen)
    fighter2.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # update display
    pygame.display.update() 

# Exit pygame
pygame.quit()
