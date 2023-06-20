import numpy as np

# numpy array 

my_list = [10,20,30,40]
my_array = np.array(my_list)

print(my_array.max())
print(my_array.min())
print(my_array.mean())

matrix_list = [[1,0,0],[0,1,0],[0,0,1],[0,0,0]]
np_matrix_list = np.array(matrix_list)

print(np_matrix_list)
print(np_matrix_list.shape)

zero = np.zeros((5,5))
print(zero)

ones = np.ones((5,5))
print(ones)

random = np.random.randint(1,100,8)
print(random)