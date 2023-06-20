import numpy as np
import matplotlib.pyplot as plt

my_numpy1 = np.linspace(0,15,20)
my_numpy2 = my_numpy1 ** 3

plt.subplot(1,2,1) # 1 row, 2 column, 1.graph 
plt.plot(my_numpy1, my_numpy2, "g--") 
plt.subplot(1,2,2)
plt.plot(my_numpy2, my_numpy1, "r*")
plt.show()