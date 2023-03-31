import matplotlib.pyplot as plt
import numpy

delhi = {
    "x":[12,13,14,15,16],
    "y":[40,50,60,70,80]
    }
mumbai={
    "a":[34,23,45,27,72],
    "b":[40,50,60,70,80]
}


plt.plot(
    delhi["x"],
    delhi["y"],
    marker="d",
    color="b"
    )
plt.plot(
     mumbai["a"],
     mumbai["b"],
    marker="s",
    color="g"
    )
plt.title("NUMBER OF PEOPLE")
plt.xlabel("people")
plt.ylabel("population")
plt.legend(["delhi","mumbai"],loc="lower left")
plt.show()
