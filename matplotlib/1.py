import numpy as np
import matplotlib.pyplot as plt

age_list = [20,25,30,35,40,45,50,55,60]
weight_list = [70,75,73,85,89,90,65,84,98]

plt.plot(age_list,weight_list, "r")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Age - Weight Graphics")
plt.show()
