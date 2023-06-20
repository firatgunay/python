import pandas as pd
import numpy as np

my_data = np.array([[10,20,30],[20,30,40],[50,50,10],[10,15,20]])

my_names = ["james", "lars", "kirk", "rob"]
my_columns = ["jan", "feb", "mar"]

my_data_frame = pd.DataFrame(my_data)
#print(my_data_frame)
my_data_frame2 = pd.DataFrame(my_data, index=my_names, columns=my_columns)
print(my_data_frame2)
print("\n")
feb_series = my_data_frame2["feb"]
print(feb_series)
print("\n")

print(feb_series.mean()) #ortalama
print("\n")

print(my_data_frame2[["jan","feb"]])
print("\n")

lars_data = my_data_frame2.loc["lars"]
print(lars_data)
print("\n")

my_data_frame2["apr"] = my_data_frame2["mar"] * 2  #yeni veri ekleme
print(my_data_frame2)
print("\n")

new_data_frame = my_data_frame2.drop("rob", axis=0) #rob un verilerini çıkarma (orijinali bozulmaz)
print(new_data_frame)
print("\n")

my_data_frame2.drop("apr", axis=1, inplace=True) #april verilerini çıkarma kalıcı şekilde
print(my_data_frame2)