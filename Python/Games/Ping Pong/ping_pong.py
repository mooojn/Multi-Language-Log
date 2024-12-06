###for moon ##change the speed of the paddles and make it faster

#modules
import pygame
import random

#ball position randomizer
def rnd():
    global direction,angle,ball_vel_x,ball_vel_y
    dir=random.choice(direction)
    ang=random.choice(angle)
    if dir==0:
        if ang==0:
            ball_vel_x,ball_vel_y=0.7,-1.4
        if ang==1:
            ball_vel_x,ball_vel_y=0.7,-0.7
        if ang==2:
            ball_vel_x,ball_vel_y=-0.7,1.4
    if dir==2:
        if ang==0:
            ball_vel_x,ball_vel_y=0.7,1.4
        if ang==1:
            ball_vel_x,ball_vel_y=0.7,0.7
        if ang==2:
            ball_vel_x,ball_vel_y=0.7,1.4

pygame.init()

#window dimensions
WIDTH,HEIGHT=1280,650
win=pygame.display.set_mode((WIDTH,HEIGHT))

#name of the game
pygame.display.set_caption("Ping Pong")

#colors
BLUE=(0,0,255)
RED=(255,0,0)
BLACK=(0,0,0)

direction=[0,1]
angle=[0,1,2]

##for the ball
radius=15
#ball dimensions
ball_x,ball_y=WIDTH/2-radius,HEIGHT/2-radius
#ball move
ball_vel_x,ball_vel_y=0.5,0.5

##for the paddle
paddle_width,paddle_height=20,120
#paddle dimensions
left_paddle_x,right_paddle_x=100-paddle_width/2,WIDTH-(100-paddle_width/2)
left_paddle_y=right_paddle_y=HEIGHT/2-paddle_height/2
#paddle move
right_paddle_vel=left_paddle_vel=0


        
run=True
##main loop
while run:
    win.fill(BLACK)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        elif i.type==pygame.KEYDOWN:
            if i.key==pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key==pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key==pygame.K_w:
                left_paddle_vel = -0.9
            if i.key==pygame.K_s:
                left_paddle_vel = 0.9
        if i.type==pygame.KEYUP:
            right_paddle_vel=0
            left_paddle_vel=0

    #ball movement controls        
    if ball_y<=0+radius or ball_y>=HEIGHT-radius:
        ball_vel_y*=-1
    if ball_x>=WIDTH-radius:
        ball_x,ball_y=WIDTH/2-radius,HEIGHT/2-radius
        rnd()
    if ball_x<=0+radius:
        ball_x,ball_y=WIDTH/2-radius,HEIGHT/2-radius
        rnd()
    
    #paddle movement controls
    if left_paddle_y>=HEIGHT-paddle_height:
        left_paddle_y=HEIGHT-paddle_height
    if left_paddle_y<=0:
        left_paddle_y=0
    if right_paddle_y>=HEIGHT-paddle_height:
        right_paddle_y=HEIGHT-paddle_height
    if right_paddle_y<=0:
        right_paddle_y=0            

    #paddle collisions
    if left_paddle_x<=ball_x<=left_paddle_x+paddle_width:
        if left_paddle_y<=ball_y<=left_paddle_y+paddle_height:
            ball_x=left_paddle_x+paddle_width
            ball_vel_x*=-1
    if right_paddle_x<=ball_x<=right_paddle_x+paddle_width:
        if right_paddle_y<=ball_y<right_paddle_y+paddle_height:
            ball_x=right_paddle_x
            ball_vel_x*=-1

    #movements
    ball_x+=ball_vel_x
    ball_y+=ball_vel_y
    right_paddle_y+=right_paddle_vel
    left_paddle_y+=left_paddle_vel

    #OBJECTS
    pygame.draw.circle(win,BLUE,(ball_x,ball_y),radius)
    pygame.draw.rect(win,RED,pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(win,RED,pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.display.update()
