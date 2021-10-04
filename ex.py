#Initialize Turtle
import turtle
import random 
d = turtle.Turtle ()

#Functions
def randomDot():
    d.color("red")
    d.begin_fill()
    d.circle(50)
    d.end_fill()
    
#Main
randomDot ()
