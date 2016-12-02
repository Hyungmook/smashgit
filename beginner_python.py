import pygame, sys
import random
pygame.init()
size = width, height = 1000, 700
screen = pygame.display.set_mode(size)
black = [0, 0, 0]

HAND_X = 500
HAND_Y = 400

class MasterHand(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(MasterHand, self).__init__()
        self.image = pygame.image.load('hohversion/handopen.png')
        self.rect = self.image.get_rect(midbottom(100, 100))
        self.x = x
        self.y = y
        self.handx = 15
        self.handy = 15
        self.width = width
        self.height = height


class Brick(pygame.sprite.Sprite):
    image = None

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        if Brick.image is None:
                Brick.image = pygame.image.load("hohversion/brick.png")
        self.image = Brick.image

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y) 
 

#the game's variables

"THE BALL"
ball_x = 10
ball_y = 10
ball_radius = 10
ball_color = [222,50,50]
ball_speed_x = 3
ball_speed_y = 5

"THE PADDLE"
# paddle_x = 20
# paddle_y = 450
# paddle_width = 60
# paddle_height = 20
# paddle_color = [20,180,180]
# paddle_speed = 10
hand = MasterHand(0, 0, 0, 0)

"THE BALL'S JUNK"
ball_img = pygame.image.load('hohversion/smashball.png')

ball_rect = ball_img.get_rect(center=(500,500))


myfont = pygame.font.SysFont("Arial", 22)
score = 0

"MAKING THE BRICKS"
brick_array = []
for i in range(1,30):
    brick1 = Brick(50*i,10)
    brick_array.append(brick1)


#allows for holding of key
pygame.key.set_repeat(20, 20)



running = True
#game loop
while running:
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.MOUSEMOTION:
        #     coordinates = pygame.mouse.get_pos() #gives (x,y) coordinates
        #     paddle_x = coordinates[0] - paddle_width/2 #sets the paddle_x variable to the first item in coordinates
        #     if paddle_x < 0:
        #         paddle_x = 0
        #     if paddle_x > screen.get_width() - paddle_width:
        #         paddle_x = screen.get_width() - paddle_width
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
            #updatd x_delta and y_delta
                x_delta = 0
                y_delta = 0
                x_delta -= 15
            if event.key == pygame.K_RIGHT:
                x_delta = 0
                y_delta = 0
                x_delta += 15
            if event.key == pygame.K_UP:
                x_delta = 0
                y_delta = 0
                y_delta -= 15
            if event.key == pygame.K_DOWN:
                x_delta = 0
                y_delta = 0
                y_delta += 15
    

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(black)
    ball_rect = ball_rect.move([ball_speed_x, ball_speed_y])

    #move the ball
    ball_y = ball_y + ball_speed_y
    ball_x = ball_x + ball_speed_x
    #check if the ball is off the bottom of the screen
    if ball_rect.top < 0 or ball_rect.bottom > height:
        ball_speed_y = -ball_speed_y
    # if ball_y > screen.get_height() - ball_radius:
    #     ball_speed_y = -ball_speed_y
    #     #do something different
    # #check if the ball hit the top of the screen
    # if ball_y < ball_radius:
    #     ball_speed_y = -ball_speed_y
    # #check if the ball hit the left side of the screen
    if ball_rect.left < 0 or ball_rect.right > width:
        ball_speed_x = -ball_speed_x
    # if ball_x < ball_radius:
    #     ball_speed_x = -ball_speed_x
    # #check if the ball hit the right side of the screen
    # if ball_x > screen.get_width() - ball_radius:
    #     ball_speed_x = -ball_speed_x

    #create imaginary rectangles around ball and paddle
    #circles are measured from the center, so have to subtract 1 radius from the x and y
    # paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    #see if the rectangles overlap
    if ball_rect.colliderect(paddle_rect):
        ball_speed_y = -ball_speed_y

    for brick in brick_array:
        if brick.rect.colliderect(ball_rect):
            score = score + 1
            brick_array.remove(brick)
            ball_speed_y = - ball_speed_y
    

    #draw everything on the screen
    score_label = myfont.render(str(score), 1, pygame.color.THECOLORS['white'])
    screen.blit(score_label, (5, 10))
    for brick in brick_array:
        screen.blit(brick.image, brick.rect)
    screen.blit(ball_img, ball_rect)
    # pygame.draw.rect(screen, paddle_color, [paddle_x, paddle_y, paddle_width, paddle_height], 0)
    #update the entire display
    pygame.display.flip()


pygame.quit()

