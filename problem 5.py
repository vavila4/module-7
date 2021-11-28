




import turtle

def drawSquare(t, sz):
   for i in range(4):
       t.forward(sz)
       t.left(90)

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")


drawSquare(alex, 50)
drawSquare(alex, 75)

wn.exitonclick()
