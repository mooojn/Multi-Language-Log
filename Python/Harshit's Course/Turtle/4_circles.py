import turtle

t=turtle.Turtle()

colors=['yellow','red','blue','green']
t.up()
t.goto(200,0)

for i in range(4):
    t.down()
    t.begin_fill()
    t.circle(50)
    t.fillcolor(colors[i])
    t.end_fill()
    t.up()
    t.bk(100)

turtle.done()


