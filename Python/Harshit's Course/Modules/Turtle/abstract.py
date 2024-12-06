import turtle

t=turtle.Turtle()

t.shape("blank")

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

t.speed(0)

for i in range(200):
    t.color(colors[i%7])
    t.pensize(i/11)           # change pensize to change the output
    t.forward(i)
    t.left(50)

turtle.done()    