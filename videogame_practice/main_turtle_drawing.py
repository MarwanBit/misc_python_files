import turtle
from turtle_practice_3 import square

main_loop_2 = True

while main_loop_2 == True:
	try:
		user_prompt = input('\nPlease type the numerical size of your square:')
		user_prompt = int(user_prompt)
		square(user_prompt)
		break
	except ValueError:
		print('That is not a number, try again')
		continue 

