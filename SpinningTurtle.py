import turtle

screen = turtle.Screen()
screen.bgcolor("lightyellow")

myTurtle=turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.color("green")

myTurtle.pensize(3)

myTurtle.penup()

forward=20

for i in range(20000):
    myTurtle.forward(forward)
    myTurtle.right(31.4)
    forward+=2.5
    myTurtle.stamp()
