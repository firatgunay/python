import pandas as pd
import numpy as np

my_dict = {"james" : 50, "lars" : 60, "kirk" : 55, "rob" : 65}
name_list = ["james", "lars", "kirk", "rob"]
age_list = [50,60,55,65]

# yapılacak iki seri de aynıdır
my_series = pd.Series(my_dict)

#my_series2 = pd.Series(name_list, age_list)
my_series2 = pd.Series(data=age_list, index=name_list)
print(my_series)
print(my_series2)