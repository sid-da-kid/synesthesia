import numpy as np

a = np.ones((5,5))
b = np.zeros((3,3))

b[1,1] = 9
a[1:4, 1:4] = b 

print(a)

# startindex:endindex:stepsize


























