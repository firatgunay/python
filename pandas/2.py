import pandas as pd
import numpy as np

my_dict = {"james" : 50, "lars" : 60, "kirk" : 55, "rob" : 65}
name_list = ["james", "lars", "kirk", "rob"]
age_list = [50,60,55,65]

numpy_array = np.array((10,20,30,40))

my_series = pd.Series(data=numpy_array, index=name_list)
print(my_series)
