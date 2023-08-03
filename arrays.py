import numpy as np

a = np.array(42)
b = np.array([
    1, 2, 3, 4, 5
    ])
c = np.array([[1, 2, 3], [4, 5, 6], [7,8,9], [19,1,12]])
d = np.array([[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6],[4,4,5]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)