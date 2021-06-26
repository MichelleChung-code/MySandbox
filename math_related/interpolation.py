import numpy as np
import scipy.interpolate as spi

# NOTE: data needs to be sorted and without noise
# Also only works for low-dimensional problems

x = np.linspace(-2, 2, 50)
y = np.cos(x) + 2 * x  # random function

spline_order_ls = [1, 3]  # just try linear and cubic first

for spline_order in spline_order_ls:
    # Determine the spline approximation
    params = spi.splrep(x, y, k=spline_order)

    # Evaluate the splines
    y_interpol = spi.splev(x, params)

    assert np.allclose(y, y_interpol)
    print(f'MSE: {sum((y - y_interpol) ** 2) / len(x):.4e}')
