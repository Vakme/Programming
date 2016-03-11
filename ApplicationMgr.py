from InputReader import InputReader 
from TrIntegrator import TrIntegrator

import sys

class ApplicationMgr():

	def __init__(self):
		obj = 0
		name = "Polynomial Integral Calculator"
		self.Welcome()

#always executed at the beginning of the app
	def Welcome(self):
		print
		print ("==================== Welcome to the PIC 2.0 ====================")
		print
		print ("You can solve an integrate using two methods")
		print

#cooperates with InputReader module. Reads input, validates it and saves as "obj"
	def Read(self):
		self.obj = InputReader()
		self.obj.Read()
		print("Do you want to see your integral?")
		self.CheckIf(self.obj.Print, None)
		print

#cooperates with TrIntegrator module. Solves an integral, shows result and compares it to scipy.integral.trapz
	def SolveIntegrator(self):
		print("Now I'm going to solve Your integral...")
		integ = TrIntegrator()
		print ("The result is %f") %integ.SolveIntegrator(self.obj)
		print ("Comparing with scipy.integral method...")
		print ("The result is %f") %integ.SolveTrapz(self.obj)
		self.EndApp()
	
#choosing function. As arguments gets two functions: one if yes, one if no
	def CheckIf(self, func1, func2):
		while 1:
			checker = raw_input("Type: Y/n ")
			if checker == "Y" or checker == "y" or checker == "yes" or checker == "Yes":
				if func1 == None:
					break
				func1()
				break
			elif checker == "N" or checker == "n" or checker == "no" or checker == "No":
				if func2 == None:
					break
				func2()
				break
			print("Try again")
		return

#terminates app
	def EndApp(self):
		print("Goodbye")
		sys.exit()
