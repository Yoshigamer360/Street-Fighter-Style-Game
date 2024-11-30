# 4/11/24 - 30/11/24
# Tutorial by Coding with Russ
# Remade by Yoshi Gamer 360

import pygame
from pygame import mixer
from fighter import Fighter

mixer.init()
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

# define game variables
introCount = 3
lastCountUpdate = pygame.time.get_ticks()
score = [0, 0]
roundOver = False
roundOverCooldown = 2000

# define fighter variables
warriorSize = 162
warriorScale = 4
warriorOffset = [72, 56]
warriorData = [warriorSize, warriorScale, warriorOffset]
wizardSize = 250
wizardScale = 3
wizardOffset = [112, 107]
wizardData = [wizardSize, wizardScale, wizardOffset]

# load music and sounds
pygame.mixer.music.load('assets/audio/music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
swordFx = pygame.mixer.Sound('assets/audio/sword.wav')
swordFx.set_volume(0.5)
magicFx = pygame.mixer.Sound('assets/audio/magic.wav')
magicFx.set_volume(0.75)

# load background image
bgImage = pygame.image.load('assets/images/background/background.jpg').convert_alpha()

# load spritesheets
warriorSheet = pygame.image.load('assets/images/warrior/Sprites/warrior.png').convert_alpha()
wizardSheet = pygame.image.load('assets/images/wizard/Sprites/wizard.png').convert_alpha()

# load victory image
victoryImg = pygame.image.load('assets/images/icons/victory.png').convert_alpha()

# define number of steps in each animations
warriorAnimationSteps = [10, 8, 1, 7, 7, 3, 7]
wizardAnimationSteps = [8, 8, 1, 8, 8, 3, 7]

# drfine font
countFont = pygame.font.Font('assets/fonts/turok.ttf', 80)
scoreFont = pygame.font.Font('assets/fonts/turok.ttf', 30)



# function for drawing text
def drawText(text, font, textCol, x, y):
    img = font.render(text, True, textCol)
    screen.blit(img, (x, y))

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
fighter1 = Fighter(1, 200, 310, False, warriorData, warriorSheet, warriorAnimationSteps, swordFx)
fighter2 = Fighter(2, 700, 310, True, wizardData, wizardSheet, wizardAnimationSteps, magicFx)



# Game loop
run = True
while run:

    clock.tick(fps)

    # draw background
    drawBg()

    # show player stats
    drawHealthBar(fighter1.health, 20, 20)
    drawHealthBar(fighter2.health, 580, 20)
    drawText('P1: ' + str(score[0]), scoreFont, red, 20, 60)
    drawText('P2: ' + str(score[1]), scoreFont, red, 580, 60)

    if introCount <= 0:
        # move fighters
        fighter1.move(screenWidth, screenHeight, screen, fighter2, roundOver)
        fighter2.move(screenWidth, screenHeight, screen, fighter1, roundOver)
    else:
        # display count timer
        drawText(str(introCount), countFont, red, screenWidth / 2, screenHeight / 3)
        # update count timer
        if (pygame.time.get_ticks() - lastCountUpdate) >= 1000:
            introCount -= 1
            lastCountUpdate = pygame.time.get_ticks()

    # update fighters
    fighter1.update()
    fighter2.update()
    
    # draw fighters
    fighter1.draw(screen)
    fighter2.draw(screen)

    # check for player defeat
    if roundOver == False:
        if fighter1.alive == False:
            score[1] += 1
            roundOver = True
            roundOverTime = pygame.time.get_ticks()
        elif fighter2.alive == False:
            score[0] += 1
            roundOver = True
            roundOverTime = pygame.time.get_ticks()
    else:
        # display victory image
        screen.blit(victoryImg, (360, 150))
        if pygame.time.get_ticks() - roundOverTime > roundOverCooldown:
            roundOver = False
            introCount = 3
            fighter1 = Fighter(1, 200, 310, False, warriorData, warriorSheet, warriorAnimationSteps, swordFx)
            fighter2 = Fighter(2, 700, 310, True, wizardData, wizardSheet, wizardAnimationSteps, magicFx)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # update display
    pygame.display.update() 

# Exit pygame
pygame.quit()
