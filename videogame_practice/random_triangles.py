import turtle as t
import math as m
import random as rand
import hex_color_generator as hex_gen_mod

main_loop = True

screen = t.Screen()
screen.bgcolor('#ADFFF1')

turtle = t.Turtle()

def random_draw_triangle():
	random_size_length = rand.randint(0,99)
	turtle.forward(random_size_length)
	turtle.right(120)
	turtle.forward(random_size_length)
	turtle.right(120)
	turtle.forward(random_size_length)
	random_size_length = 0

while main_loop == True:

	turtle.color(hex_gen_mod.hex_generator())
	screen_color = hex_gen_mod.hex_generator()
	screen.bgcolor(screen_color)

	random_draw_triangle()
	
	turtle.penup()
	turtle.goto(rand.randint(-249,249),rand.randint(-249,249))
	turtle.tilt(rand.randint(0,359))
	turtle.lt(rand.randint(0,359))
	turtle.rt(rand.randint(0,359))
	turtle.pendown()