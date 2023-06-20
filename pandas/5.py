import pandas as pd
import numpy as np

my_dict = {"james" : [40,30,np.nan], "kirk":[20,np.nan,50], "lars":[30,50,40]}

my_data_frame = pd.DataFrame(my_dict)
print(my_data_frame)
print("\n")

print(my_data_frame.dropna()) #kayıp verileri siler
print(my_data_frame.dropna(axis=1))
print("\n")

my_new_data_frame = my_data_frame.fillna(25) # olmayan verileri doldurur

print(my_new_data_frame)