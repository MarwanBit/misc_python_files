import turtle as turtle
import random as rand
import hex_color_generator as hex_gen

#defines objects 
turtle_god = turtle.Turtle()
screen = turtle.Screen()

turtle.color = ('orange', 'green')
turtle.bgcolor('#4AFFED')

main_loop = True
global_color_variable = 0

while main_loop == True:

    #Square
    for i in range (0,4):
        turtle_god.forward(30)
        turtle_god.right(90)
    #Repositions to a random area and changes the color    
    turtle_god.penup()
    turtle_god.goto(rand.randint(-200, 200), rand.randint(-200, 200))
    turtle_god.pendown()
    global_color_variable = hex_gen.hex_generator()
    turtle.bgcolor(global_color_variable)
  
