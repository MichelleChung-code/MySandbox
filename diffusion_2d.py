import numpy as np
from scipy.ndimage.filters import laplace
import numexpr as ne


# https://en.wikipedia.org/wiki/Diffusion_equation


def evolve_matrix(input_m, output_m, dt, D=1):
    laplace(input_m, output_m, mode='wrap')  # use periodic boundary condition
    str_eval = 'output_m * D * dt + input_m'
    ne.evaluate(str_eval, out=output_m)


if __name__ == '__main__':
    mat_shape = (100, 100)
    num_iter = 10

    output_m = np.zeros(mat_shape)
    input_m = np.zeros(mat_shape)
    lower = int(mat_shape[0] * 0.1)
    upper = int(mat_shape[0] * 0.2)

    input_m[lower:upper, lower:upper] = 0.001

    for i in range(num_iter):
        evolve_matrix(input_m, output_m, dt=0.1)
        input_m, output_m = output_m, input_m

    print(input_m)
    print(output_m)
