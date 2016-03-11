#validates input

class InputValidator:
	
	def __init__(self):
		self.validationFlag = False		#flag used to tell if validation gone well

#checks if read value is proper
	#value		value to check
	#canNegative	tells if value can be negative
	#typeChecker	string being a type target type of value
	def validate(self, value, canNegative, typeChecker = ""):
		self.validationFlag = False
		value = self.checkType(value, typeChecker)
		if value == "False":
			return value
		if canNegative == False:
			value = self.checkSign(value)
			if value == "False":
				return value
		self.validationFlag = True
		return value
			
#checks and converts a value to a proper type. Default is float
	def checkType(self, value, typeChecker):
			try:
				if typeChecker == "int" :
					value = int(value)
				else:
					value = float(value)
				return value
			except ValueError:
				print "ValueError: try again"
				return "False"

#checks sign and returns error if minus
	def checkSign(self, value):
			if value < 0:
				print ("SignError: this number can't be negative. Try again")
				return "False"
			else:
				return value
