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
        # pg.sprite.Sprite.__init__(self, img_file, initial_x, initial_y)
        self.game = game

        self.initial_x = initial_x
        self.initial_y = initial_y

        # self.set_initial_position()


    # def set_initial_position(self):
    #     # set_position method is inherited from Sprite class
    #     self.set_position(self.initial_x,self.initial_y)
    #     self.velocity = 0.0
    #     self.angle = None

    def move(self):
        '''
        Move this game object one unit forward in the direction of its velocity.
        :return:
        '''
        x_vel,y_vel = as_cartesian(self.velocity, self.angle)
        self.set_position(self.x + int(x_vel), self.y + int(y_vel))


    def update(self,pressed_keys):
        self.move()



class BallDeflector(GameObject):

    def deflect_ball(self,ball,side_hit):
        '''
        Deflect a ball that has collided with this object.
        :param ball:
        '''

        if side_hit == 'RIGHT' or side_hit == 'LEFT':
            ball.angle = (180-ball.angle) % 360
        elif side_hit == 'BOTTOM' or side_hit == 'TOP':
            ball.angle = (- ball.angle) % 360

        self.shunt(ball)

    def shunt(self, ball):
        while ball.colliding_with(self):
            ball.move()
            if (ball.x < 0) or (ball.y < 0):
                foobar

class EndLine(BallDeflector):

    def deflect_ball(self, ball, side_hit):
        print ("hit an endline")
        if side_hit == 'UP':
            sys.quit()
        else:
            # Shouldn't happen. Must have miscalculated which side was hit, since this is an endline
            raise Exception(side_hit)

class Ball(GameObject):

    default_velocity = 10.0 #Number of pixels the ball should move per game cycle
    initial_x = 0
    initial_y = 0

    position = initial_x, initial_y
    

    def update(self,pressed_keys):
        self.move()
        if self.in_play:
            for game_object in self.game.game_objects:
                side_hit = self.colliding_with(game_object)
                if side_hit:
                    game_object.deflect_ball(self, side_hit)

    def generate_random_starting_angle(self):
        '''
        Generate a random angle that isn't too close to straight up and down or straight side to side
        :return: an angle in degrees
        '''
        angle = randint(10,75)
        debug_print('Starting ball angle: ' + str(angle) + ' degrees')
        return angle

    def set_position(self):
    	self.set_pos = self.position
    	self.velocity = self.default_velocity

    	self.angle = self.generate_random_starting_angle()
    	self.in_play = True

    def colliding_with(self,game_object):

        if (self.x < game_object.x):
            left, right = self, game_object
        else:
            left, right = game_object, self
        x_distance = right.x - (left.x + left.width)

        if (self.y < game_object.y):
            bottom, top = self, game_object
        else:
            bottom, top = game_object, self
        y_distance = top.y - (bottom.y+ bottom.height)

        if (x_distance > 0) or (y_distance > 0):
             # no overlap
            return False
        else:
            # figure out which side of game_object self hit
            # first, special cases of horizontal or vertical approach angle
            special_cases = {0: 'LEFT', 90: 'BOTTOM', 180: 'RIGHT', 270: 'TOP'}
            if self.angle in special_cases:
                return special_cases[self.angle]
            else:
                # Decide base on self's y position at the point where they intersected in the x-dimension
                (x_vel, y_vel) = as_cartesian(self.velocity, self.angle)
                slope = y_vel / x_vel
                # go x_distance units either forward or back in x dimension; multiply by slope to get offset in y dimension
                y_at_x_collision = self.y - sign(y_vel)*math.fabs(x_distance * slope)
                if (self.angle < 90):
                    # coming from below left, check if top of self was below game_object
                    if y_at_x_collision + self.height < game_object.y:
                        return 'BOTTOM'
                    else:
                        return 'LEFT'
                elif (self.angle < 180):
                    # coming from below right, check if top of self was below game_object
                    if y_at_x_collision + self.height < game_object.y:
                        return 'BOTTOM'
                    else:
                        return 'RIGHT'
                elif self.angle < 270:
                    # coming from above right, check if bottom of self was above game_object
                    if y_at_x_collision > game_object.y + game_object.height:
                        return 'TOP'
                    else:
                        return 'RIGHT'
                else:
                    # coming from above right, check if bottom of self was above game_object
                    if y_at_x_collision > game_object.y + game_object.height:
                        return 'TOP'
                    else:
                        return 'LEFT'

    def deflect_ball(self, ball, side_hit):
        # balls don't deflect other balls
        pass


#Creating a hand that DEFLECTS NOW MOTHER FUQER
class MasterHand(BallDeflector):
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


class Brick(BallDeflector):
	def deflect_ball(self, ball, side_hit):
		BallDeflector.deflect_ball(self, ball, side_hit)
		selfgame.game_objects.remove(self)

class Game(object):
	def __init__(self,
		width = 1000,
		height = 700,
		wall_width = 10,
		brick_height = 40):

		self.score = [0,0]
		self.width = width
		self.height = height
		self.hit_count = 0

		self.balls = [Ball(img_file= ball_img, initial_x = 0, initial_y = 0, game = self)]
		self.walls = [BallDeflector(initial_x = 0, initial_y = 0, img_file = wall_imgs[1], game = self),
		BallDeflector(initial_x = 0, initial_y = 0, img_file = wall_imgs[0], game = self),
		BallDeflector(initial_x = self.width - wall_width, initial_y = 0, img_file = wall_imgs[0], game = self),
		Endline(initial_x = 0, initial_y = self.height - wall_width, img_file = wall_imgs[1], game= self)]

		self.bricks = []

		for x in range(6):
			for b in range(11):
				self.bricks.append(Brick(
					initial_x = self.width - wall_width - (brick_height*(x+1)),
					initial_y = (b*brick_height),
					img_file = brick_imgs,
					game = self))

		self.game_objects = self.walls + self.bricks + self.balls

	def draw(self):
		for game_object in self.game_objects:
			game_object.draw()

	def increment_hit_count(self):
		self.hit_count += 1
		if self.hit_count == 3:
			for ball in self.balls:
				ball.velocity += 1





#Setting the caption
pg.display.set_caption("Smash time!")

#Starting the pygame


def main():

	game_over = False

	hand = MasterHand(everything)

	while True:

		x_delta = 0
		y_delta = 0
		ball_img = pg.image.load("hohversion/ball.png")
		# wall_imgs = [pg.image.load('vertical_wall.png'),
		# pg.image.load('horizontal_wall.png')]
		# brick_imgs = pg.image.load('brick.png')

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
		DISPLAYSURF.blit(ball_img, (Ball.set_position(Ball)))
		#DISPLAYSURF.blit(wall_imgs[0], )

		pg.display.update()
		fpsClock.tick(FPS)

	pg.quit()

if __name__ == '__main__':
	gameExit = False
	main()