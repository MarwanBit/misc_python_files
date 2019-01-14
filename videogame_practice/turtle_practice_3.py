import turtle
import math



def square(side_length):
	screen = turtle.Screen()
	drawing_turtle = turtle.Turtle()
	drawing_turtle.getscreen().bgcolor("#8B6969")
	for i in range(0,4):
		drawing_turtle.forward(side_length)
		drawing_turtle.right(90)
	screen.exitonclick()
	

def turtle_reset():
	drawing_turtle.reset()


