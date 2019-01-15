import turtle as turtle
import random as rand

turtle_god = turtle.Turtle()

turtle.color = ('orange', 'green')
turtle.bgcolor('#4AFFED')

main_loop = True
random_number_for_iteration = ''
hex_alphabet_in_python = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def rand_hexadecimal_number_generator():
   random_number_for_iteration = '#'
   for i in range(0,7):
        random_number_for_iteration = random_number_for_iteration + str(hex_alphabet_in_python[rand.randrange(0,15)])
   

while main_loop == True:
    for i in range (0,4):
        turtle_god.forward(30)
        turtle_god.right(90)
        
    turtle_god.penup()
    turtle_god.goto(rand.randint(-200, 200), rand.randint(-200, 200))
    turtle_god.pendown()
    random_number_for_iteration = ''
    rand_hexadecimal_number_generator()
    turtle.bgcolor(random_number_for_iteration)
  
