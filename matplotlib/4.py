import numpy as np
import matplotlib.pyplot as plt

my_numpy1 = np.linspace(0,15,20)
my_numpy2 = my_numpy1 ** 3

my_figure = plt.figure()
my_axes = my_figure.add_axes([1,1,0,5,0,5])
my_axes.plot(my_numpy1,my_numpy2, "g--")
my_axes.set_xlabel("X-Data")
my_axes.set_ylabel("Y-Data")
plt.show()