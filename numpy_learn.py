import numpy as np

#with normal arrays 
a = [1,2,3,4]
b = [10,20,30,40]

print(a+b) #wit normal arrays this would just concatenate and create on big array

#with numpy

a1 = np.array([1,2,3,4])
b1 = np.array([10,20,30,40])
sum_arr = a1+b1
print(sum_arr)

print(sum_arr.ndim, sum_arr.shape, sum_arr.dtype)

#Indexing and slicing