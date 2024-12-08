import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,0] ])
arr2 = np.array([1,2,3,4,5,6,7,8])
# printing the shape of the array
print(arr.shape)

# reshaping the array
arr3 = arr2.reshape(2,4)
print(arr3)

# checking the base of the array
print(arr3.base)

# iterating through the array
for x in np.nditer(arr):
    print(x)
    