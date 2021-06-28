import scipy.integrate as sci
import numpy as np
import sympy as sy


def f_test(x):
    return np.cos(x) + 4 * x


# integration methods available to use
dict_integration_methods = {'fixed_quad': sci.fixed_quad,  # fixed gaussian quadrature
                            'quad': sci.quad,  # adaptive quadrature
                            'romberg': sci.romberg,  # romberg integration
                            }


def numerical_integration(f, a, b, type):
    """

    Args:
        f: <function> to integrate
        a: <float> lower interval bound
        b: <float> upper interval bound
        type: <str> type of numerical integrator to use.  Needs to be a key in dict_integration_methods

    Returns:
        result of specified scipy integrate method call
    """
    if not dict_integration_methods.get(type, False):
        raise KeyError('Invalid Numerical Integration Type Requested')

    return dict_integration_methods[type](f, a, b)


def monte_carlo_estimation(num_estimations: int, f, a: float, b: float):
    """

    Args:
        num_estimations: <int> number of random x values within (a, b) to evaluate the integration function at
        f: <function> to integrate
        a: <float> lower interval bound
        b: <float> upper interval bound

    Returns:
        <float> integration estimation

    """
    # get random values of x between integral limits
    x = np.random.uniform(low=a, high=b, size=(num_estimations,))

    # return the average function value over the integration interval multiplied by the interval length
    return np.sum(f(x)) / len(x) * (b - a)


def sympy_integration(a, b, f, x=sy.Symbol('x')):
    """
    Evaluate the integral using Sympy

    Args:
        a: <float> lower interval bound
        b: <float> upper interval bound
        f: <sympy> function to evaluate
        x: <sympy.Symbol> for x

    Returns:
        <float> integration result of f, evaluated using a and b limits
    """
    integrated = sy.integrate(f, x)

    Fa = integrated.subs(x, a).evalf()
    Fb = integrated.subs(x, b).evalf()

    # or using dictionary for limits
    a_lim = sy.Symbol('a_lim')
    b_lim = sy.Symbol('b_lim')

    integrated_symbolic = sy.integrate(f, (x, a_lim, b_lim))
    dict_sol = integrated_symbolic.subs({a_lim: a, b_lim: b}).evalf()

    # results in the same value
    assert Fb - Fa == dict_sol == sy.integrate(f, (x, a, b))
    assert integrated.diff() == f  # derivative of the antiderivative yields the original function

    return Fb - Fa


if __name__ == '__main__':
    a = 0.5
    b = 9.5
    print(numerical_integration(f_test, a, b, 'fixed_quad'))
    print(numerical_integration(f_test, a, b, 'quad'))
    print(numerical_integration(f_test, a, b, 'romberg'))
    print(monte_carlo_estimation(10000, f_test, a, b))

    x = sy.Symbol('x')
    f = sy.cos(x) + 4 * x
    print(sympy_integration(a, b, f))
