import tkinter as tk 
from block_info import BlockInfo 
from tkinter import ttk

class GraphicalInterface(tk.Tk):
	'''Class which inherits from root and is used for the frame of the GUI'''

	def __init__(self):
		'''Initializes the class along with Tkinter Inheritance from tk.Tk'''
		#Initializes the tk.Tk Inheritance, gives this object tk.Tk's attributes and methods
		super().__init__()

		#Titles the root Window 
		self.title("Bobby Maximus Training Program")

		#Creating the BackGround Image
		self.bg_image = tk.PhotoImage('images/bobby_maximus.jpg')
		self.image = self.bg_image
		self.bg_label = ttk.Label(self, image= self.image)
		self.bg_label.pack()

		#Creates the frame which is then placed inside of the root window
		#self.fr_width = 400
		#self.fr_height = 400
		#self.frame = tk.Frame(self, width= self.fr_width, height= self.fr_height)
		#self.frame.pack()


user_interface = GraphicalInterface()
user_interface.mainloop()




