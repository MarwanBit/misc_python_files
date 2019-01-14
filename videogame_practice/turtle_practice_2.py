import turtle

my_turtle = turtle.Turtle()

def rectangle(height, width, color):
	my_turtle.color(color)
	turtle.begin_fill()
	for i in range(1,3):
		my_turtle.forward(width)
		my_turtle.right(90)
		my_turtle.forward(height)
		my_turtle.right(90)
	turtle.end_fill()


rectangle(100, 50, 'blue')
turtle.done()
