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


def is_normal(arr, check_is_lognormal=False):
    """
    Return whether the input array is normally distributed
    Based on whether p-value of skew, kurtosis, and normal tests are above 0.05

    Args:
        arr: <np.Array> to evaluate
        check_is_lognormal: <bool> if wanting to check whether distribution is lognormal

    Returns:
        <bool> whether the input is normally distributed
    """
    if check_is_lognormal:
        arr = np.log(arr)
        print('Checking for log-normality...')

    norm_p = scs.normaltest(arr).pvalue
    kurt_p = scs.normaltest(arr).pvalue
    skew_p = scs.skewtest(arr).pvalue

    pprint({'Norm test p-value': norm_p,
            'Kurt test p-value': kurt_p,
            'Skew test p-value': skew_p})

    return all(x >= 0.05 for x in (norm_p, kurt_p, skew_p))


if __name__ == '__main__':
    arr = np.random.normal(loc=50, scale=10, size=1000)
    pprint(get_key_statistics(arr))
    print(is_normal(arr, check_is_lognormal=False))
