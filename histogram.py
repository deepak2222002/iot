import matplotlib.pyplot as plt
import numpy

p=numpy.array([20,10,50,70,35])
plt.hist(p,width=0.5)
plt.xlabel("people")
plt.ylabel("days")
plt.show()