import scipy.stats as scs
import numpy as np
from pprint import pprint


def get_key_statistics(arr):
    """
    Extracts information from scipy.stats describe method

    Args:
        arr: <np.Array> to extract statistics from

    Returns:
        <dict> of size, min, max, mean, std, skew, and kurtosis
    """
    stats = scs.describe(arr)
    return {'size': stats.nobs,
            'min': stats.minmax[0],
            'max': stats.minmax[1],
            'mean': stats.mean,
            'std': np.sqrt(stats.variance),
            'skew': stats.skewness,
            'kurtosis': stats.kurtosis}


if __name__ == '__main__':
    arr = np.random.normal(loc=50, scale=10, size=1000)
    pprint(get_key_statistics(arr))
