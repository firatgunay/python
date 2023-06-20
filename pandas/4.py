import pandas as pd
import numpy as np

my_data = np.array([[10,20,30],[20,30,40],[20,50,10],[10,15,20]])

my_names = ["james", "lars", "kirk", "rob"]
my_columns = ["jan", "feb", "mar"]

my_data_frame = pd.DataFrame(my_data, index=my_names, columns=my_columns)

boolean_frame = my_data_frame > 25
#print(boolean_frame)
print("\n")
print(my_data_frame[boolean_frame])
print("\n")

print(my_data_frame[my_data_frame["mar"] > 25])
print("\n")

new_data_frame = my_data_frame.reset_index() # index e çevirir
print(new_data_frame)