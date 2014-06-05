import pygame, sys, random
from pygame.locals import *

pygame.init()

#Screen Attributes
screen = pygame.display.set_mode((640,400), 0, 32)
pygame.display.set_caption("Coin Collector 0.1")

#Images
background = pygame.image.load("data/img/background.png").convert()

#Character
char_posit = "data/img/character_basicPos.png"
character = pygame.image.load(char_posit).convert_alpha()

charPositionX = 300
charPositionY = 150

#Coin
coin = pygame.image.load("data/img/coin.png").convert_alpha()

coin_position_x = random.randint(0,560)
coin_position_y = random.randint(0,400)

#Loading Font And Rendering Text
score = 0
font = pygame.font.Font(None, 24)
text = font.render("Score: %s" %(score), 1, (10,15,30))

screen.blit(text, (320,0))
	
#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type != KEYDOWN:
            char_posit = "data/img/character_basicPos.png"
        else:
            if event.key == K_LEFT:
                charPositionX = charPositionX - 8
                char_posit = "data/img/character_movingLeft.png"
 
            if event.key == K_RIGHT:
                charPositionX = charPositionX + 8
                char_posit = "data/img/character_movingRight.png"

            if event.key == K_UP:
                charPositionY = charPositionY - 8
                char_posit = "data/img/character_movingUp.png"                

            if event.key == K_DOWN:
                char_posit = "data/img/character_basicPos.png"                
                charPositionY = charPositionY + 8


    screen.blit(background, (0,0))

    character = pygame.image.load(char_posit).convert_alpha()
    screen.blit(character, (charPositionX,charPositionY))
    screen.blit(coin, (coin_position_x, coin_position_y))

   #Collision Detection
    if charPositionX < coin_position_x + 25 and charPositionX + 16 > coin_position_x and charPositionY < coin_position_y + 25 and charPositionY + 31 > coin_position_y:
        coin_position_x = random.randint(0,600)
        coin_position_y = random.randint(0,400)

        score = score + 1

        screen.blit(coin, (coin_position_x,coin_position_y))

    text = font.render("Score: %s" %(score), 1, (10,15,30))
    screen.blit(text, (320,0))

    pygame.display.update()
    
