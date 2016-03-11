import math

import scipy.integrate
#solves integrator
class TrIntegrator:

	def __init__ (self):
		self.score = 0.0

#solves integrate. As an argument takes validated InputReader object
	def SolveIntegrator(self, obj):			#works well if delta_x == 1
		if obj.delta_x == 0.0:
			delta_x = 1.0
		self.score = ((self.Polynomial(obj, obj.x_0) + self.Polynomial(obj, obj.x_0 + obj.delta_x))*obj.delta_x)/2
		return self.score

#returns result of polynomial in particular point
	def Polynomial(self, obj, value):
		print("Solving polynomial of %2.2f...") %value
		score = 0.0
		power = obj.highestNumber
		for factor in obj.x_n:
			power -= 1
			score += factor * pow(value, power)
		return score
		
#solves integrate using scipy.integrate.trapz
	def SolveTrapz(self, obj):
		a = self.Polynomial(obj, obj.x_0)
		b = self.Polynomial(obj, obj.x_0 + obj.delta_x)
		print("Solving...")
		self.score = scipy.integrate.trapz([a, b])
		return self.score
