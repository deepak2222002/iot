import matplotlib.pyplot as plt
import numpy

y=numpy.array([30,30,40])
mylabels=["delhi","mumbai","jaipur"]
myexplode=[0.2,0,0]
plt.pie(y, labels=mylabels,explode=myexplode)
plt.title("number of people")

plt.show()
