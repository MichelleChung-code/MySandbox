# Using scipy optimize
import scipy.optimize as spo
import cvxpy as cp

x = cp.Variable()
y = cp.Variable()
obj = cp.Minimize(cp.square(x - y))
constraints_ls = [-10 <= x, x <= 10, -10 <= y, y <= 10]

prob = cp.Problem(obj, constraints_ls)

# confirm that this is convex
assert prob.is_dcp()  # will return True if it is a valid convex

prob.solve()


def obj_func(tup_x_y):
    z = (tup_x_y[0] - tup_x_y[1]) ** 2
    return z


# scipy implementation
scipy_x_y = spo.brute(obj_func, ((-10, 10.1, 0.1), (-10, 10.1, 0.1)), finish=None)

assert prob.value == obj_func(scipy_x_y)
