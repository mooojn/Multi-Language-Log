import turtle
t=turtle.Turtle()
t.pensize(3)
t.speed(0)
def rectangle(color):
    pass

t.up()
t.goto(0,-300)
t.down()
t.goto(0,200)
t.begin_fill()
t.fd(100)
t.right(90)
t.fd(150)
t.right(90)
t.fd(100)
t.fillcolor("gray")
t.end_fill()

t.bk(100)
t.begin_fill()
t.bk(200)
t.right(90)
t.fd(150)
t.left(90)
t.fd(200)
t.fillcolor("green")
t.end_fill()
for i in range(5):
 
        # moving turtle 100 units forward
        t.forward(100)
 
        # rotating turtle 144 degree right
        t.right(144)

t.hideturtle()

turtle.done()