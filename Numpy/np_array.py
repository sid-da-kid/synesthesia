import numpy as np

a = np.array([1,2,3], dtype = 'int16')
b = np.array([[0.5,1.0,1.5],[2.0,2.5,3.0]])

# Getting info
print(b.ndim)
print(b.dtype)
print(b.itemsize) # (bytes)
print(a.nbytes)
print(b[0, 0])
 



































