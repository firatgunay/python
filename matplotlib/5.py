import numpy as np
import matplotlib.pyplot as plt

my_numpy1 = np.linspace(0,15,20)
my_numpy2 = my_numpy1 ** 3

#fig, axes = plt.subplots()
my_numpy3 = np.linspace(0,15,20)
my_numpy4 = my_numpy3 ** 2
#axes.plot(my_numpy3,my_numpy4, "g--")
#axes.plot(my_numpy4,my_numpy3, "r--")

new_fig, new_axes = plt.subplots()
new_axes.plot(my_numpy3, my_numpy3 + 2, color = "#B81DCD", linewidth = 2.4)
new_axes.plot(my_numpy3, my_numpy3 + 3, color = "#1DCDCA", linewidth = 1.4)
new_axes.plot(my_numpy3, my_numpy3 + 4, color = "blue", linewidth = 1.4, linestyle = "-.")
new_axes.plot(my_numpy3, my_numpy3 + 5, color = "green", linewidth = 1.4, linestyle = ":")

#figürü kaydetme
new_fig.savefig("myfig.png", dpi=200)
plt.show()