import pygame as pg
import sys
from pygame.locals import *

#Setting the colors
black = pg.Color(0, 0, 0)
blue = pg.Color(0, 0, 255)
green = pg.Color(0, 128, 0)
red = pg.Color(255, 0, 0)
yellow = pg.Color(255, 255, 0)
white = (255, 255, 255)

pg.init()

#FPS of the game
FPS = 30
fpsClock = pg.time.Clock()

#Making the tab
DISPLAYSURF = pg.display.set_mode((1000, 500))

#This is to fill the display with white
DISPLAYSURF.fill(white)
#This is to draw a black line from x coordinate 200-800 and y coordinate 400
pg.draw.line(DISPLAYSURF, black, (800, 400), (200, 400))

#Creating a hand
handImg = pg.image.load('meleelight/src/assets/hand/handopen.png')
handx = 15
handy = 15
direction = 'right'

#Setting the caption
pg.display.set_caption("Smash time!")

#Starting the pygame
while True:

	if direction == 'right':
		handx += 1
		

	DISPLAYSURF.blit(handImg, (handx, handy))

	for event in pg.event.get():
		if event.type == QUIT:
			pg.quit()
			sys.exit()
		pg.display.update()
		fpsClock.tick(FPS)
