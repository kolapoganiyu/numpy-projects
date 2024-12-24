# Doing exercises in numpy from w3 resource
import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([[1,2,3], [4,5,6]])
arr3 = np.array([[[1,2,3], [3,4,5], [5,6,7]]])


# 1. Get numpy version and Build info
print("This is the version",np.__version__)

# 2. Help for Numpy Add Functions
# np.info(np.add)

# 3. Test if any are non-zero
test = np.any(arr1)

if test:
    print("This is has values that are non-zero")
    print("This i s vlaue in nfhlfhkfhjhghgjghkf")