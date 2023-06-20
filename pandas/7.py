import pandas as pd
import numpy as np

my_dict1 = {
    "name" : ["A","B","C","D"],
    "sports" : ["basketball", "football", "tennis", "running"],
    "calories" : [100,200,300,400]
}
my_frame1 = pd.DataFrame(my_dict1, index=[0,1,2,3])
print(my_frame1)
print("\n")

my_dict2 = {
    "name" : ["E","F","G","H"],
    "sports" : ["basketball", "football", "tennis", "running"],
    "calories" : [200,50,330,440]
}
my_frame2 = pd.DataFrame(my_dict2, index=[4,5,6,7])
print(my_frame2)
print("\n")

my_dict3 = {
    "name" : ["I","J","K","L"],
    "sports" : ["basketball", "football", "tennis", "running"],
    "calories" : [300,150,320,410]
}
my_frame3 = pd.DataFrame(my_dict3, index=[8,9,10,11])
print(my_frame3)
print("\n")

# üç data frame'i birleştirme (concatenation and merge)
# 1 concatenation
my_concat_frame = pd.concat([my_frame1,my_frame2,my_frame3])
print(my_concat_frame)
print("\n")

# 2 merge
my_merge_frame = pd.merge(my_frame1,my_frame2,on="sports")
print(my_merge_frame)
print("\n")