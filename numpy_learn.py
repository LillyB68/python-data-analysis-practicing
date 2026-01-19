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

#print(sum_arr.ndim, sum_arr.shape, sum_arr.dtype)

#Indexing and slicing
#-The indecing is same as lists
#slicing
arr = np.array([5,10,15,20])
#print(arr[1:3])
#boolean indexing 
marks = np.array([45,67, 89, 32, 50])
#print(marks[marks >= 50])

#practicing indexing and slicing
scores = np.array([34, 78, 56, 90, 45, 67])

passed_well = scores[scores >= 60]
failed = scores[scores < 50]
passed = scores[scores >= 50]

pass_count = len(passed)
print(pass_count)


#Vectorised operations numpy 
new = scores + 5
print(np.std(new))



