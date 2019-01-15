import random as rand

def hex_generator():
	random_hex_number_for_iteration_list = ['#']
	hex_alphabet_in_python = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	random_hex_color_number_for_iteration = ''
	for i in range(0,6):
		random_hex_number_for_iteration_list.append(hex_alphabet_in_python[rand.randrange(0,15)])
	for i in random_hex_number_for_iteration_list:
		random_hex_color_number_for_iteration += str(i)
	return random_hex_color_number_for_iteration


