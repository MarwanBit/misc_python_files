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

	def describe_block(self, block_number):
		'''
		This function takes the argument of block_number and then uses it to print the dictionary containing
		the information for that specified block. There are exceptions built in to prevent a bad user experience
		through the use of exceptions.
		'''

		#These two lines intialize a one_way_flag variable for a loop and define the list that will be accessed.
		loop_boolean = True
		block_number_list = (self.block_1, self.block_2, self.block_3, self.block_4, self.block_5, self.block_6)

		'''
		This block loops through a try except block. The try block trys to use the block_number argument as an
		index in accessing a gym block. If the user inputs a string that can't be converted into a integer a value
		error exception is called and the user gets another chance to correct themselves. If the user types a number
		not in range than an Index Error is called which gives the users an opportunity to correct themselves.
		'''
		while loop_boolean == True:
			try:
				block_number = int(block_number)
				'''
				Block number - 1 adjusts the index from our intuitive counting starting at one to python index 
				counting.
				'''
				for day, schedule in block_number_list[block_number -1].items():
					print ("\n" + str(day) + " : " + str(schedule))
				print("\n that is the schedule for block " + str(block_number) + ".")
				break
			except ValueError:
				user_input = input("\nThat is not a number, try again:")
				block_number = user_input 
			except IndexError:
				user_input = input("\nYour number is out of range, try again:")
				block_number = user_input
				
		
			


			
my_regiment = BlockInfo()
my_regiment.describe_block('2')
			
