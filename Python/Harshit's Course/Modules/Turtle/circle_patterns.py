import turtle


t=turtle.Turtle()

def draw_circle(px,py,rad,color):

    t.up()
    t.goto(px,py)
    t.down()
    
    t.begin_fill()
    t.circle(rad)
    t.fillcolor(color)
    t.end_fill()

draw_circle(0,-50,50,"green")
draw_circle(0,300,25,"green")

draw_circle(200,200,50,"orange")
draw_circle(0,-300,25,"orange")

draw_circle(-200,200,50,"blue")
draw_circle(300,0,25,"blue")

draw_circle(-200,-200,50,"red")
draw_circle(-300,0,25,"red")

draw_circle(200,-200,50,"yellow")

t.hideturtle()


turtle.done()
