#Asks user for data 
from InputValidator import InputValidator

class InputReader:

	def __init__(self):
		self.highestNumber = 0;
		self.x_n = []
		self.x_0 = 0
		self.delta_x = 0
		self.validator = InputValidator()

#reads values using proper methods
	def Read(self):
		print
		print("Now I am going to ask You about Your intergate")
		self.readHighestNumber()
		self.readXn()
		self.readX0()
		self.readDelta() 
		print

#validation methods will be looping until the right value won't be given
	def readHighestNumber(self):
		while 1:
			self.highestNumber = self.validator.validate(raw_input("The highest power of x: "), False, "int")
			if self.validator.validationFlag == True:
				break
			
	def readXn(self):
		for i in range(0, self.highestNumber):
			while 1: 
				temp = self.validator.validate(raw_input("Factor %d: " %(self.highestNumber - i-1)),True)
				if self.validator.validationFlag == True:
					self.x_n.append(temp)
					break
			
	def readX0(self):
		while 1:
			self.x_0 = self.validator.validate(raw_input("x_0: "), True)
			if self.validator.validationFlag == True:
				break
	
	def readDelta(self):
		if self.highestNumber == 1:
			self.delta_x = 1.0
		else: 
			while 1:
				self.delta_x = self.validator.validate(raw_input("Delta x: "), False)
				if self.validator.validationFlag == True:
					break
#prints input data		
	def Print(self):
		print("The highest power of x: %d") %self.highestNumber
		print("The factors: ")
		print self.x_n
		print("x_0 = %2.2f, delta_x = %2.2f") %(self.x_0, self.delta_x)
