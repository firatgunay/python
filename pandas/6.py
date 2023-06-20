import pandas as pd
import numpy as np

#gruplama

salary_dict = {
    "programming language": ["python","python","python","java","java","swift"],
    "name" : ["A","B","C","D","E","F"],
    "salary" :[100,90,80,70,60,50]
}

salary_frame = pd.DataFrame(salary_dict)
print(salary_frame)
print("\n")

group_object = salary_frame.groupby("programming language")
print(group_object.count())
print("\n")
print(group_object.mean("salary"))
print("\n")
print(group_object.min("salary"))
print("\n")

print(group_object.describe()) # genel özet tablosu çıkarır.

