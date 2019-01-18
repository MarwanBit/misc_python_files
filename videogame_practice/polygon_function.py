import turtle as t 
import random as rand
import hex_color_generator as hn
import time as time

#Creates a function that creates a polygon based off of the arguments side number (number of sides) and side_length
def create_polygon(side_number, side_length):
	for i in range(0, side_number):
		drawing_turtle.forward(side_length)
		drawing_turtle.right(float(360/side_number))

#one_way_flag_variable used to create an infinite loop for the program
main_loop_one_way_flag = True 

#Main loop for the program
while main_loop_one_way_flag == True:

	#Asks if you want to begin or exit
	user_input = input('do you want to begin(y/n)?')

	'''If you anwser 'y' then you are asked for input that is then used to create a polygon,
	a screen is then created, and the program waits 30 seconds before exiting'''
	if user_input == 'y':
		side_number_user_input = input("Type the amount of sides wanted in your polygon:")
		side_length_user_input = input("Type the length of your polygon sides:")
		drawing_turtle = t.Turtle()
		screen = t.Screen()
		create_polygon(int(side_number_user_input), int(side_length_user_input))
		screen_color = hn.hex_generator()
		screen.bgcolor(screen_color)
		time.sleep(30)
		break

	#If you type 'n' then you are asked to confirm, you're then exited from the program
	elif user_input == 'n':
		user_input = input('Are you sure (y/n)?')
		if user_input == 'y':
			break
		elif user_input == 'n':
			continue 

	#if you don't type either y or n you are asked to try typing an input again
	else:
		user_input = input('Try again:')
		continue 






