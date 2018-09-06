import matplotlib.pyplot as plt
import numpy as np

X= np.linspace(-np.pi,np.pi,100,endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.plot(X,C,X,S)
#plt.plot([1,2,3],[5,6,9])
plt.xlabel("X")
plt.ylabel("Cosine and Sine")
plt.title("Demo Plot in Python for Understanding purpose\n")
plt.axis([0,5,-1,1])
plt.show()