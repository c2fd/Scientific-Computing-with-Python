import numpy as np
x = np.array([1,2,3])
z = x
z[2] = 1
print(x)
print(x is z)
print( 1 in x)
print(type(x))

