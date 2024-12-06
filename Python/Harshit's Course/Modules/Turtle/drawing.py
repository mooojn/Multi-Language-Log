import turtle

t=turtle.Turtle()
win=turtle.Screen()
# win.bgcolor("black")

t.shape("turtle")
t.color("blue","green")

                            # '1' : slowest, '0' : fastest
t.speed(1)                  # controls the pen drawing speed

t.begin_fill()              # start of color fill

## drawing square
# for i in range(4):          
#     t.fd(100)
#     t.left(90)

### syntax  mandatory   optional   optional
# t.circle(  radius  ,   extent  ,  steps    )               

## drawing circle
# t.circle(100)                

## drawing semi circle
# t.circle(100,extent=180)      

## drawing triangle
t.circle(100,steps=3)        

t.hideturtle()              # hides the turtle

t.fillcolor('red')          # color to fill

t.end_fill()                # end of color fill


t.reset()                   # reset's the complete turtle
                            # drawing and settings

t.speed(1)              
t.up()                      # makes the pen go up does'nt draw anything

t.goto(0,-100)              # moves the pen in x,y coordinates

t.down()                    # makes the pen down no you can draw

t.circle(100)


turtle.done()
