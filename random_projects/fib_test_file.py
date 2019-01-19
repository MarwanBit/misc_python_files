fib_file = 'fib_file.txt'

with open(fib_file, 'r') as fib_numbers:
	fib_file_var = fib_numbers.readlines()
	fib_local_list = []
	for line in fib_file_var:
		fib_local_list.append(line)
	print(fib_local_list)
	fib_numbers.close()