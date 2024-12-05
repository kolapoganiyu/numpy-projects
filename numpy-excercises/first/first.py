import numpy as np


# working with # 3D array
arr = np.array([[[1,2,3,4,5], [5,4,3,2,1]], [[10,9,8,7,6], [6,7,8,9,0]]], )

# confirming the dimensions
print(arr.ndim)
# printed 3 from the first item
print(arr[0, 1, 2])

# slicing through
print(arr[1, 0, ::2])

# copying and viewing the array
newArray1 = arr.copy()
newArray2 = arr.view()

# checking the bases of the array
print(newArray1.base)   # will not have a base because it owns the value
print(newArray2.base)   # will have a base because it does not own the value
'''
if changes are made on 'newArray1', it will not be reflected on the original array
but
if changes are mode on 'newArray2, it will be reflected on the original array
'''





