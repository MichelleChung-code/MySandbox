import numpy as np

x = np.linspace(-2, 2, 50)
y = np.cos(x) + 2 * x  # random function

# set up basis
order = 3
mat = np.zeros((order + 1, len(x)))  # of shape (order + 1, len(x))
mat[0, :] = 1
mat[1, :] = x
mat[2, :] = x ** 2
mat[3, :] = np.cos(x)  # exploit that we know the function is cos-sine

# fit with least squares
params = np.linalg.lstsq(mat.T, y, rcond=None)[0]
assert np.allclose(y, params @ mat)