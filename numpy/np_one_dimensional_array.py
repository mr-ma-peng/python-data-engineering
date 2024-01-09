import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])
c = a + b
print(c)
print(type(c))
print(c.dtype)
print(c.size)
print(c.ndim)
print(c.shape)


print('-------------------------------------------------')
u = [1, 0]
v = [0, 1]
z = []

for n, m in zip(u, v):
    z.append(n + m)

print(z)

print('-----------multiplication with a scalar------------')
y = np.array([1, 2])
z = 2*y
print(z)

print('---------universal function---------')
a = np.array([1, -1, 5, -1])
print(a.mean())
print(a.max())
print(np.linspace(-2, 2, num=5))