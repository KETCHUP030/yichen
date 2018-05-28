import numpy as np
from numpy.linalg import inv
A = np.array([[1, 0.5, 5],[2.3, 2, 3],[4, 1, 1.7]])
b = np.array([[1, 2, 3]])
#c = np.transpose(b)
x = np.matmul(inv(A),np.transpose(b))
print(x)