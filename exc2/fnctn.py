# Written by: Kartik Chari
# Date: 02 Sept 2018
# This function plots the 2d graph of the exression h(t)=3*pi*(10^-lambda)

# importing libraries
import matplotlib.pyplot as plt
import numpy as np

# preparing a linspace t consisting of 100 points from 0 to 2pi
t = np.linspace(0,2*np.pi,100,endpoint=True)

lmbd = 5*np.sin(2*np.pi*t)
h = 3*np.pi*np.power(10,-lmbd)

plt.xlabel("time")
plt.ylabel("3*pi*exp(-lambda)")
plt.title("Plot for the Periodic expression\n")
plt.axis([0,1,-1000,1000000])

plt.plot(t,h)
plt.show()