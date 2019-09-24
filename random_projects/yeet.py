import random 

empty_data_list = []
random.seed(42)

for i in range(400):
	empty_data_list.append(random.randint(1,20))

print(empty_data_list) 

histogram_dictionary = {}

for i in range(1,21):
	histogram_dictionary[str(i)] = ''  

for k in histogram_dictionary.keys():
	histogram_dictionary[k] = str(empty_data_list.count(int(k)))

print(histogram_dictionary)





