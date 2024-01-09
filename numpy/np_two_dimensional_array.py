import numpy as np


print('-------create 2d array------')
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

A = np.array(a)
print(A)
print(A.ndim)
print(A.shape)
print(A.size)

print(A[1][1])
print(A[1, 1])
print(A[1, 0:3])
print(A[0:2, 2])

print('-----------basic operations--------')
x = np.array([[1, 0],[0, 1]])
y = np.array([[2, 1],[1, 2]])
z = x + y
print(z)
print(2*z)
print(x*y)
print(np.dot(x, y))



