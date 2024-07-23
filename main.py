import turtle
from turtle import *
import random
turtle.colormode(255)
tim=Turtle()
tim.speed("fast")
tim.color("grey")
tim.hideturtle()
pencolor


directions = [90,0,-90]
tim.pensize(12)

def walk():
    tim.forward(25)
last_color = None

def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

def random_direction():
    angle=random.choice(directions)
    if angle == 90:
        tim.left(90)
    elif angle == -90:
        tim.right(90)
    else:
        tim.right(0)


for i in range(50):
    tim.color(random_colour())
    walk()
    random_direction()













screen=Screen()
screen.exitonclick()