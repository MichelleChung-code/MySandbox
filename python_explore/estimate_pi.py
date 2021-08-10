from timing_dec import timing
import multiprocessing as mp

import random
import numpy as np


# multiprocessing internally seeds when it sees the python random package in the namespace
# however, if using the numpy random module... need to make sure to explicitly seed.

def calc_inside_quarter_circ(num_experiments):
    """
    Return the number of tries that ended up inside the area of the quarter circle

    Args:
        num_experiments: <int> or <float> number of trials to run.  If <float>, will be converted to <int>

    Returns:
        <int> number of tries that ended up in the quarter circle

    """
    res = 0
    for i in range(int(num_experiments)):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        res += (x ** 2 + y ** 2 <= 1)  # adds 1 for the bool True condition

    return res


def calc_inside_quarter_circ_np(num_experiments):
    """
    Return the number of tries that ended up inside the area of the quarter circle
    Version of calc_inside_quarter_circ but vectorizing with numpy

    Args:
        num_experiments: <int> or <float> number of trials to run.  If <float>, will be converted to <int>

    Returns:
        <int> number of tries that ended up in the quarter circle

    """
    np.random.seed()  # explicitly set seed to ensure that each of the forked processes generate a unique sequence of random numbers

    x = np.random.uniform(0, 1, int(num_experiments))
    y = np.random.uniform(0, 1, int(num_experiments))
    return np.sum(x ** 2 + y ** 2 <= 1)


@timing
def estimate_pi_multiprocess(num_experiments, use_numpy=False):
    """
    Estimates the value of pi - monte carlo randomized experiments

    Args:
        num_experiments: <int> total number of experiments to run across all cores

    Returns:
        <float> the estimated value for pi
    """
    num_cores = mp.cpu_count()
    pool = mp.Pool(processes=num_cores)

    worker_samples = num_experiments / num_cores
    per_process = [worker_samples] * num_cores

    quarter_circ_res = pool.map(calc_inside_quarter_circ, per_process) if not use_numpy else pool.map(
        calc_inside_quarter_circ_np, per_process)
    pi = sum(quarter_circ_res) * 4 / num_experiments

    return pi


if __name__ == '__main__':
    num_experiments = 10_000_000
    print(estimate_pi_multiprocess(num_experiments))  # does not use numpy
    print(estimate_pi_multiprocess(num_experiments, use_numpy=True))  # vectorizes with numpy
