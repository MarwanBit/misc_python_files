class BlockInfo():
	'''
	This block provides all information needed to run the program.
	This includes block lengths, block layouts, all workouts and their workout type.
	In addition basic methods such as describe a block are provided; all list editing
	and schedule information will be provided in the main program loop.
	'''
	
	def __init__(self):
		'''
		This __init__ method provides all the information needed for further calculations.
		This module will be imported into the main program loop and then this class well be the 
		master class to a more specific subclass that contains methods needed to edit schedules.
		'''
		self.block_1 = 	{
							'Monday' : ('Warmup','Max Test', 'Finisher', 'Cooldown'),
							'Tuesday' : ('Warmup', 'Challenge', 'Finisher', 'Cooldown'),
							'Wednesday' : ('Warmup','Max Test', 'Finisher', 'Cooldown'),
							'Thursday' : ('Warmup', 'Challenge', 'Finisher', 'Cooldown'),
							'Friday' : ('Warmup', 'Challenge', 'Finisher', 'Cooldown'),
							'Saturday' : ('Rest or Recovery (CardioVascular)'),
							'Sunday' : ('Rest or Recovery (CardioVascular)')
						}

		self.block_2 = 	{
							'Monday' : ('Warmup','Circuit-Style', 'Finisher', 'Cooldown'),
							'Tuesday' : ('Warmup', 'Interval', 'Finisher', 'Cooldown'),
							'Wednesday' : ('Warmup', 'IWT', 'Finisher', 'Cooldown'),
							'Thursday' : ('Warmup', 'Time Trial', 'Cooldown'),
							'Friday' : ('Warmup', 'Circuit-Style', 'Finisher', 'Cooldown'),
							'Saturday' : ('Rest or Warmup', 'Interval', 'Finisher', 'Cooldown'),
							'Sunday' : ('Rest or Recovery (CardioVascular)')
						}

		self.block_3 = 	{
							'Monday' : ('Warmup', 'Strength and Power', 'Finisher', 'Cooldown'),
							'Tuedsay' : ('Warmup', 'Interval', 'Finisher', 'Cooldown'),
							'Wednesday' : ('Warmup', 'Strength and Power', 'Finisher', 'Cooldown'),
							'Thursday' : ('Warmup', 'TimeTrial', 'Cooldown'),
							'Friday' : ('Warmup', 'Circuit-Style', 'Finisher', 'Cooldown'),
							'Saturday' : ('Rest or Recovery (Weighted)'),
							'Sunday' :('Rest or Recovery (CardioVascular)')
						}

		self.block_4 = 	{
							'Monday' : ('Warmup', 'Mass Gain', 'Finisher', 'Cooldown'),
							'Tuesday' : ('Warmup', 'Time Trial', 'Cooldown'),
							'Wednesday' : ('Warmup', 'Mass Gain', 'Finisher', 'Cooldown'),
							'Thursday': ('Warmup', 'Interval', 'Finisher', 'Cooldown'),
							'Friday' : ('Warmup', 'IWT', 'Finisher', 'Cooldown'),
							'Saturday' : ('Rest or Recovery (Weighted'),
							'Sunday' : ('Rest or Recovery (CardioVascular')
						}

		self.block_5 = 	{
							'Monday' : ('Warmup', 'Circuit-Style', 'Finisher', 'Cooldown'),
							'Tuesday' : ('Warmup', 'IWT', 'Cooldown'),
							'Wednesday' : ('Warmup', 'Interval', 'Finisher', 'Cooldown'),
							'Thursday': ('Warmup', 'IWT', 'Cooldown'),
							'Friday' : ('Warmup', 'Circuit-Style', 'Finisher', 'Cooldown'),
							'Saturday' : ('Rest or Warmup', 'Time Trial', 'Finisher', 'Cooldown'),
							'Sunday' : ('Rest or Recovery (CardioVascular')
						}

		self.block_6 =	{
							'Monday' : ('Warmup', 'Max Test or Challenge', 'Finisher', 'Cooldown'),
							'Tuesday' : ('Warmup', 'Time Trial', 'Cooldown'),
							'Wednesday' : ('Warmup', 'Max Test or Challenge', 'Finisher', 'Cooldown'),
							'Thursday': ('Warmup', 'Interval', 'Finisher', 'Cooldown'),
							'Friday' : ('Warmup', 'Circuit-Style', 'Finisher', 'Cooldown'),
							'Saturday' : ('Rest or Warmup', 'IWT', 'Finisher', 'Cooldown'),
							'Sunday' : ('Rest or Recovery (CardioVascular)')
						}

		#This block provides the length of a block in terms of weeks
		self.block_length = [0,1,2,3]

		#Initializes empty lists for weeks of block 1 
		self.block_1_week_1 = []
		self.block_1_week_2 = []
		self.block_1_week_3 = []
		self.block_1_week_4 = []

		#Initializes empty lists for weeks of block 2 
		self.block_2_week_1 = []
		self.block_2_week_2 = []
		self.block_2_week_3 = []
		self.block_2_week_4 = []

		#Initializes empty lists for weeks of block 3
		self.block_3_week_1 = []
		self.block_3_week_2 = []
		self.block_3_week_3 = []
		self.block_3_week_4 = []

		#Initializes empty lists for weeks of block 4
		self.block_4_week_1 = []
		self.block_4_week_2 = []
		self.block_4_week_3 = []
		self.block_4_week_4 = []

		#This block creates a list for all ascii letters for use in a comparison
		self.ascii_characters = 'abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\\'

	def describe_block(self, block_number):
		loop_boolean = True
		while loop_boolean == True:
			try:
				#This block iterates through the schedule information and prints it in a readable format
 				block_number_list = [self.block_1, self.block_2, self.block_3, self.block_4, self.block_5, self.block_6]
				block_number = int(block_number) - 1 
				block_dictionary_in_use = block_number_list[block_number]
				for k, v in block_dictionary_in_use.items():
					#This prints the contents of the dictionary
					print('\n' + str(k) + ' : ' + str(v))
				loop_boolean == False
			except ValueError:	
				block_number_input_letter_string = ''		
				for i in list(block_number):
					if i in self.ascii_characters:
						#The line below creates a list of letters in block_number
						block_number_input_letter_string += str(i)						
						print('\nThat is not a number!')
						continue
				user_input = input('\nType a number or "q" to quit! :')
				if block_number_input_letter_string in self.ascii_characters:
					continue
				elif type(user_input) == str and user_input == 'q':
					quit 
				elif float(user_input) > 5:
					print('\nThat number is to big!')
				elif float(user_input) >=1 and float(user_input) <= 5:
					block_number = user_input
			except IndexError:
				print('\nThat number is to big')
				continue
			else:
				break

					
			


			
my_regiment = BlockInfo()
my_regiment.describe_block('1')
			
