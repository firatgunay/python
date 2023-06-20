import numpy as np
import matplotlib.pyplot as plt

my_numpy1 = np.linspace(0,15,20)
my_numpy2 = my_numpy1 ** 3

plt.plot(my_numpy1, my_numpy2, "g--")  
plt.show()