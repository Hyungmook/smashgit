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
    def __init__(self, x, y, width, height):
        super(MasterHand, self).__init__()
        self.image = pg.image.load('hohversion/handopen.png')
        self.rect = self.image.get_rect()
        self.rect.center = (HAND_X, HAND_Y)
        self.x = 0
        self.y = 0
        self.handx = 15
        self.handy = 15

        self.width = 10
        self.height = 75

	# def hit_position(self, ball):
	# 	virtual_height = self.height + ball.height
	# 	y_dist = ball.y + ball.height - self.y
	# 	pct = y_dist / float(virtual_height)
	# 	return pct


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.width = width
        self.height = height

        self.image = pg.Surface([width, height])
        self.image.fill((red))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Ball(pg.sprite.Sprite):

    change_x = 0
    change_y = 0
    walls = None


    def __init__(self, x, y, walls):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('hohversion/smashball.jpg')
        self.rect = self.image.get_rect()
        self.rect.y = BALL_Y
        self.rect.x = BALL_X

    def update(self):
        old_x = self.rect.x
        new_x = old_x + self.change_x
        self.rect = new_x

        #Wall x collision
        collide = pg.sprite.spritecollide(self, self.walls, False)
        if collide:
            self.rect.x = old_x
            self.change_x *= -1

        old_y = self.rect.y
        new_y = old_y + self.change_y
        self.rect.y = new_y

        #Wall y collision
        collide = pg.sprite.spritecollide(self, self.walls, False)
        if collide:
            self.rect.y = old_y
            self.change_y *= -1

        if self.rect.x < -20 or self.rect.x > screen_width + 20:
            self.change_x = 0
            self.change_y = 0


    # def calcpos(self, rect, vector):
    #     (angle,z) = vector
    #     (dx,dy) = (z*math.cos(angle), z*math.sin(angle))
    #     return rect.move(dx,dy)


	


#Setting the caption
pg.display.set_caption("Smash time!")

screen_width = 1000
screen_height = 700
DISPLAYSURF = pg.display.set_mode((screen_width, screen_height))


wall_list = pg.sprite.Group()
all_sprites = pg.sprite.Group()
movingsprites = pg.sprite.Group()
#Top
wall = Wall(0,0,screen_width,10)
wall_list.add(wall)
all_sprites.add(wall)
#Bottom
wall = Wall(0,screen_height - 10, screen_width, screen_height)
wall_list.add(wall)
all_sprites.add(wall)

hand = MasterHand(0, 0, screen_width, 0)

ball = Ball(-50, -50, wall_list)
movingsprites.add(ball)
all_sprites.add(ball)

while True:

    x_delta = 0
    y_delta = 0

    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()

        elif event.type == pg.KEYDOWN:
            if ball.change_y == 0:
                ball.rect.x = screen_width / 2
                ball.rect.y = random.randrange(10, screen_height - 0)

                ball.change_y = random.randrange(-5,6)
                ball.change_x = random.randrange(5, 10)

                if(random.randrange(2) == 0):
                    ball.change_x *= -1

    movingsprites.update()


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
    all_sprites.draw(screen)
    pg.display.update()
    fpsClock.tick(FPS)

pg.quit()
