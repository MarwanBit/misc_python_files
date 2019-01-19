#This is a memoization version of the fibonnaci sequence

#This defines a collection of fib_numbers in the sequence after they have been solved they're appended onto this list
fib_number_dictionary = {}

#This is the path for the txt file that holds the fibonnaci numbers on each line
fib_file = 'fib_file.txt'

#This var holds the index for what fib_number is being calculated
starting_fib = 1

#This is the one way flag variable for creating the infinite loop used in this program
main_loop = True

#Functions that defines how the fibonnaci sequence works 
def fib(n):

	if n in fib_number_dictionary:
		return fib_number_dictionary[n]

	elif n <= 2:
		fib_dictionary_value = 1
		fib_number_dictionary[n] = fib_dictionary_value
		return fib_dictionary_value

	elif n > 2:
		fib_dictionary_value = fib(n-1) + fib(n-2)
		fib_number_dictionary[n] = fib_dictionary_value
		return fib_dictionary_value

while main_loop == True:

	#Creates the prompt that describes the instructions ot the user
	prompt = 'type "quit" to quit, "open" to read the file,'
	prompt += '\n"next number" to store the next fib number,'
	prompt += '\n"clear" to clear the file,'
	prompt += '\nanything else will result in an error'
	prompt += '\n============\n(input):'

	user_input = input(prompt)

	if user_input == 'quit':
		break

	#This part needs work, only type the recorded fib numbers in a session after a clear!!!
	elif user_input == 'open':
		with open(fib_file, 'r') as fib_numbers:
			fib_file_var = fib_numbers.readlines()
			fib_local_list = []
			for line in fib_file_var:
				line = line.replace('\n', '')
				fib_local_list.append(line)
			print(fib_local_list)
			fib_numbers.close()

	elif user_input == 'next number':
		with open(fib_file, 'a') as fib_numbers:
			fib_number = fib(starting_fib)
			fib_numbers.write(str(fib_number) + '\n')
			starting_fib = starting_fib + 1
			fib_numbers.close()
		print('\nYou stored: ' + str(fib_number))

	elif user_input == 'clear':
		with open(fib_file, 'w') as fib_numbers:
			pass
		starting_fib_number = 1
		print('\n')

	elif user_input == 'print fib_number':
		print(starting_fib_number)

	else:
		print('\nError, try again!')

	