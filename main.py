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

# Function for the velocity and the angle
def as_cartesian(velocity,angle):
    if angle is None:
        return 0,0
    else:
        return veloc

def sign(num):
    if num >= 0:
        return 1
    else:
        return -1

#For a game object in pygame
class GameObject(pg.sprite.Sprite):

    def __init__(self, img_file = None, initial_x = 0, initial_y = 0, game = None):
        pyglet.sprite.Sprite.__init__(self, img_file, initial_x, initial_y)
        self.game = game

        self.initial_x = initial_x
        self.initial_y = initial_y

        self.set_initial_position()


    def set_initial_position(self):
        # set_position method is inherited from Sprite class
        self.set_position(self.initial_x,self.initial_y)
        self.velocity = 0.0
        self.angle = None

    def move(self):
        '''
        Move this game object one unit forward in the direction of its velocity.
        :return:
        '''
        x_vel,y_vel = as_cartesian(self.velocity, self.angle)
        self.set_position(self.x + int(x_vel), self.y + int(y_vel))


    def update(self,pressed_keys):
        self.move()




#Creating a hand
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


		# menu_items = ('Start', 'Quit')
		# gm = GameMenu(DISPLAYSURF, menu_items)
		# gm.run()
		

		DISPLAYSURF.fill(black)
		#always do an updated here of hand.handx and hand.handy		
		hand.handx+=x_delta
		hand.handy+=y_delta
		DISPLAYSURF.blit(hand.image, (hand.handx, hand.handy))

		pg.display.update()
		fpsClock.tick(FPS)

	pg.quit()

if __name__ == '__main__':
	gameExit = False
	main()