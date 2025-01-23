#1
import turtle
s=turtle.Turtle()
for i in range(4):
    s.forward(100)
    s.left(90)

#2
import turtle
s=turtle.Turtle()
s.forward(300)
s.left(90)
s.forward(300)
s.left(90)
s.forward(300)
s.left(90)
s.forward(300)
s.left(90)
s.hideturtle()
s.showturtle()

#3
import turtle
s=turtle.Turtle()
s.forward(100)
s.penup() #picks up the turtle pen--> invisible line
s.right(90)
s.forward(100)
s.right(90)
s.pendown() #makes the line visible
s.forward(100)
