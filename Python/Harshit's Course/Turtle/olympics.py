import turtle

t=turtle.Turtle()

color='gray'

t.up()
t.goto(200,0)

t.pensize(10)    
for i in range(4):
    t.down()
    t.color(color)
    t.circle(100)
    
    t.up()
    t.bk(100)


turtle.done()


