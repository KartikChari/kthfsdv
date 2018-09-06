# Written by: Kartik Chari
# Date: 02 Sept 2018
# This file creates an interactive interface which controls the live plot of the exression h(t)=3*pi*(10^-lambda)

import matplotlib.pyplot as plt
#from matplotlib.widgets import Slider, Button, CheckButtons, TextBox
import numpy as np
import time

class PlotTwist:
	def __init__(self):
		self.f=1

	def exp_h(self, t):
		lmbd = 5*np.sin(2*np.pi*t)
		return 3*np.pi*np.power(10,-lmbd)

	def plotData(self,n):
		#n=100
		plt.ion()

		# preparing a linspace t consisting of 100 points from 0 to 2pi
		t = np.linspace(0,1,100,endpoint=True)
		H = self.exp_h(t)

		_t = []
		_h = []

		for i in range (0,100,1):
			_t = np.append (_t,t[i])
			_h = np.append (_h,H[i])

			plt.xlabel("time")
			plt.ylabel("3*pi*exp(-lambda)")
			plt.title("Plot for the Periodic expression\n")
			plt.axis([0,1,-1000,1000000])
			plt.plot(_t, _h)
			plt.show()
			plt.pause(0.05)

if __name__ == "__main__":
	k = PlotTwist()
	k.plotData(100)
