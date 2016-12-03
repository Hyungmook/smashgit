import pygame, sys
import random
pygame.init()
size = width, height = 1000, 700
screen = pygame.display.set_mode(size)
empty = pygame.Surface(size)
black = [0, 0, 0]

everything = pygame.sprite.Group()

class MasterHand(pygame.sprite.Sprite):
    def __init__(self, hand):
        self.image = pygame.image.load('hohversion/handopen.png')
        self.handx = 0
        self.handy = 0
        self.rect = self.image.get_rect(midbottom = (500, 750))
        


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
ball_speed_x = 5
ball_speed_y = 5

"THE PADDLE"
hand = MasterHand(everything)
x_delta = 0
y_delta = 0

"THE BRICKS"
wall_speed_x = 2
wall_speed_y = 2
delta_wall_x = 0
delta_wall_y = 0


"THE BALL'S JUNK"
ball_img = pygame.image.load('hohversion/smashball.png').convert()
ball_trans = ball_img.get_at((0,0))
ball_img.set_colorkey(ball_trans)
ball_rect = ball_img.get_rect(center=(500,500))

"FOR THE FONT SCORE"
myfont = pygame.font.SysFont("Arial", 22)
score = 0

"MAKING THE BRICKS"
ran = random.randint(45, 60)
brick_array = []
for i in range(1,11):
    for j in range(1, 11):
        brick1 = Brick(90*i,40*j)
        brick_array.append(brick1)


#allows for holding of key
pygame.key.set_repeat(20, 20)

credits_timer = 250

theme = "hohversion/3-26-battle-champion-.mp3"
theme2 = "hohversion/092 Lavender Town.mp3"
pygame.mixer.pre_init(44100, -16, 2, 2048)


while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
pygame.mixer.music.load(theme)
# pygame.mixer.music.play(loops = 5, start = 0.0)
pygame.mixer.music.play(-1) 


running = True
game_over = False
#game loop
while running == True:
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.QUIT:
            running = False

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
            

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            x_delta -=2
            hand.handx += x_delta
            hand.rect = hand.rect.move([hand.handx, 0])
            hand.handx = 0
        if keys_pressed[pygame.K_RIGHT]:
            x_delta +=2
            hand.handx += x_delta
            hand.rect = hand.rect.move([hand.handx, 0])
            hand.handx = 0



            

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(black)
    ball_rect = ball_rect.move([ball_speed_x, ball_speed_y])
    

    #move the ball
    if ball_rect.top < 0 or ball_rect.bottom > height:
        ball_speed_y = -ball_speed_y

    if ball_rect.left < 0 or ball_rect.right > width:
        ball_speed_x = -ball_speed_x


    "I wanted to make a game_over"
    if ball_rect.bottom == height:
        running = False

    if ball_rect.colliderect(hand.rect):
        ball_speed_y = -ball_speed_y
        pygame.mixer.Sound("hohversion/SSBB_Grab.wav").play()


    for brick in brick_array:
        if brick.rect.colliderect(ball_rect):
            if ball_rect.top < brick.rect.bottom or ball_rect.bottom > brick.rect.top:
                ball_speed_y = - ball_speed_y
            elif ball_rect.right > brick.rect.left or ball_rect.left < brick.rect.right:
                ball_speed_x = - ball_speed_x
            score = score + 1
            brick_array.remove(brick)

    if score == 10:
        for brick in brick_array:
            brick.rect = brick.rect.move([wall_speed_x, wall_speed_y])
            if brick.rect.left < 0 or brick.rect.right > width:
                wall_speed_x = -wall_speed_x
            if brick.rect.top < 0 or brick.rect.bottom > 300:
                wall_speed_y = -wall_speed_y
        screen.blit(secret, (40, 10))

    if score >= 15 and score < 30:
        for brick in brick_array:
            brick.rect = brick.rect.move([wall_speed_x, -wall_speed_y])
            if brick.rect.left < 0 or brick.rect.right > width:
                wall_speed_x = -wall_speed_x
                # tempx = -wall_speed_x
            if brick.rect.top < 0 or brick.rect.bottom > 400:
                wall_speed_y = -wall_speed_y
                # tempy = -wall_speed_y
        screen.blit(lb_label, (40, 10))

    if score >= 30 and score < 60:
        for brick in brick_array:
            brick.rect = brick.rect.move([wall_speed_x, -wall_speed_y])
            if brick.rect.left < 0 or brick.rect.right > width:
                wall_speed_x = -wall_speed_x
            if brick.rect.top < 0 or brick.rect.bottom > 600:
                wall_speed_y = -wall_speed_y
        screen.blit(A_label, (40, 10))

    if score >= 60 and score < 65:
        screen.blit(C_label, (40, 10))

    if score >= 65 and score < 70:
        ball_speed_y = 6
        ball_speed_x = 6
        # if ball_rect.top < 0 or ball_rect.bottom > height:
        #     ball_speed_y = -ball_speed_y
        # if ball_rect.left < 0 or ball_rect.right > width:
        #     ball_speed_x = -ball_speed_x
        # if ball_rect.colliderect(hand.rect):
        #     ball_speed_y = -ball_speed_y
        # for brick in brick_array:
        #     if brick.rect.colliderect(ball_rect):
        #         if ball_rect.top < brick.rect.bottom or ball_rect.bottom > brick.rect.top:
        #             ball_speed_y = - ball_speed_y
        #         elif ball_rect.left < brick.rect.right or ball_rect.right > brick.rect.left:
        #             ball_speed_x = - ball_speed_x
        #         score = score + 1
        #         brick_array.remove(brick)
        screen.blit(Twist_label, (500, 0))
        if ball_rect.bottom == height:
                running = False


    # if game_over:
    #     myfont = pygame.font.SysFont("monospace", 50)
    #     label = myfont.render("Game over!", 1, (255,255,0))
    #     screen.blit(label, (300, 320))
    #     if credits_timer > 0:
    #         credits_timer -= 1
    #     else:
    #         break

    "Labels"
    secret = myfont.render("Did you catch that?", 1, pygame.color.THECOLORS['white'])
    score_label = myfont.render(str(score), 1, pygame.color.THECOLORS['white'])
    lb_label = myfont.render("Looking Good!", 1, pygame.color.THECOLORS['white'])
    A_label = myfont.render("Amazing!", 1, pygame.color.THECOLORS['white'])
    everything.clear(screen, empty)
    C_label = myfont.render("Congratulations! You're basically done", 1, pygame.color.THECOLORS['white'])
    Twist_label = myfont.render("OR ARE YOU?", 1, pygame.color.THECOLORS['red'])


    #draw everything on the screen
    everything.clear(screen, empty)
    screen.blit(score_label, (5, 10))
    for brick in brick_array:
        screen.blit(brick.image, brick.rect)
    screen.blit(ball_img, ball_rect)
    screen.blit(hand.image, hand.rect)
    everything.update()
    everything.draw(screen)
    pygame.display.flip()

pygame.mixer.music.stop()
pygame.mixer.music.load(theme2)
pygame.mixer.music.play(-1)

while running == False:
    go_label = myfont.render("Game over. Jk! Everyone's a winner at heart. Press TAB to quit", 1, pygame.color.THECOLORS['black'])
    screen.fill(pygame.color.THECOLORS['white'])
    screen.blit(go_label, (300, 350))
    pygame.display.flip()
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                pygame.quit()
