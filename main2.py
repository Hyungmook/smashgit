import pygame as pg
import sys
from pygame.locals import *
from pygame.sprite import *
from random import *

#Setting the colors
black = pg.Color(0, 0, 0)
blue = pg.Color(0, 0, 255)
green = pg.Color(0, 128, 0)
red = pg.Color(255, 0, 0)
yellow = pg.Color(255, 255, 0)
white = pg.Color(255, 255, 255)

pg.init()

#variable that equals the entire group
everything = pg.sprite.Group()

#FPS of the game
FPS = 60
fpsClock = pg.time.Clock()

#Making the tab
DISPLAYSURF = pg.display.set_mode((1000, 700))


#***TEST***This is to draw a black line from x coordinate 200-800 and y coordinate 400
#pg.draw.line(DISPLAYSURF, black, (800, 400), (200, 400))

#Creating a general position
HAND_X = 500
HAND_Y = 400

#Create a general position
BALL_X = 200
BALL_Y = 200

#Creating a hand that DEFLECTS NOW MOTHER FUQER
class MasterHand(pg.sprite.Sprite):
	def __init__(self, hand):
		super(MasterHand, self).__init__()
		self.image = pg.image.load('hohversion/handopen.png')
		self.rect = self.image.get_rect()
		self.rect.center = (HAND_X, HAND_Y)
		self.x = 0
		self.y = 0
		self.handx = 15
		self.handy = 15

	def hit_position(self, ball):
		virtual_height = self.height + ball.height
		y_dist = ball.y + ball.height - self.y
		pct = y_dist / float(virtual_height)
		return pct

class Ball(pg.sprite.Sprite):
    def __init__(self, vector):
        pg.sprite.Srite.__init__(self)
        self.image = pg.image.load('hohversion/smashball.jpg')
        self.rect = self.image.get_rect()
        self.rect.center = (BALL_X, BALL_Y)
        self.vector = vector

    def update(self):
        pos = self.calcpos(self.rect, self.vector)
        self.rect = pos

    def calcpos(self, rect, vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx,dy)


	


#Setting the caption
pg.display.set_caption("Smash time!")

#Starting the pygame


def main():

    game_over = False

    hand = MasterHand(everything)

    while True:

        x_delta = 0
        y_delta = 0

        for event in pg.event.get():
        	if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        		sys.exit()

			# if event.type == pg.KEYDOWN:
			# 	if event.key == pg.K_LEFT:
			# 		#updatd x_delta and y_delta
			# 		x_delta = 0
			# 		y_delta = 0
			# 		x_delta -= 15
			# 	if event.key == pg.K_RIGHT:
			# 		x_delta = 0
			# 		y_delta = 0
			# 		x_delta += 15
			# 	if event.key == pg.K_UP:
			# 		x_delta = 0
			# 		y_delta = 0
			# 		y_delta -= 15
			# 	if event.key == pg.K_DOWN:
			# 		x_delta = 0
			# 		y_delta = 0
			# 		y_delta += 15

        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_LEFT]:
            x_delta -=20
        if keys_pressed[K_RIGHT]:
           x_delta +=20
# if keys_pressed[K_UP]:
# 	y_delta -=20
# if keys_pressed[K_DOWN]:
# 	y_delta +=20


        DISPLAYSURF.fill(black)

        hand.handx+=x_delta
        hand.handy+=y_delta
        DISPLAYSURF.blit(hand.image, (hand.handx, hand.handy))
        DISPLAYSURF.blit(Ball.image, (Ball.rect, Ball.vector))
        pg.display.update()
        fpsClock.tick(FPS)

    pg.quit()

if __name__ == '__main__':
	gameExit = False
	main()