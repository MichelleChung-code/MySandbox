import scipy.integrate as sci
import numpy as np


def f_test(x):
    return np.cos(x) + 4 * x


# integration limits
dict_integration_methods = {'fixed_quad': sci.fixed_quad,  # fixed gaussian quadrature
                            'quad': sci.quad,  # adaptive quadrature
                            'romberg': sci.romberg,  # romberg integration
                            }


def numerical_integration(f, a, b, type):
    if not dict_integration_methods.get(type, False):
        raise KeyError('Invalid Numerical Integration Type Requested')

    return dict_integration_methods[type](f, a, b)

if __name__ == '__main__':
    a = 0.5
    b = 9.5
    print(numerical_integration(f_test, a, b, 'fixed_quad'))
    print(numerical_integration(f_test, a, b, 'quad'))
    print(numerical_integration(f_test, a, b, 'romberg'))
