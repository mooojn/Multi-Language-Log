import turtle

moon=turtle.Turtle()        # turtle object

moon.color("blue","green")  # 1st is the line color and 
                            # 2nd is turtle color

moon.shape("turtle")        # changing the shape of drawing pen
                            # options "classic/default","turtle",
                            # and many more


win=turtle.Screen()         # screen object

win.title("moojn")          # name of the app
win.bgcolor("white")        # for background color

# win.bgpic("Nv2.gif")      # to place a background picture
                            # file must be in "gif" format


### moving the turtle

moon.fd(200)                # fd and forward are same
moon.left(90)               # changes the head of the turtle by angle's
moon.fd(200)
moon.bk(400)                # bk, back, backward are same

turtle.done()               # mandatory after ending a turtle program
