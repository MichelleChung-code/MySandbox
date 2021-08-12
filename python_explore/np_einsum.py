import numpy as np
from timing_dec import timing


# https://ajcr.net/Basic-guide-to-einsum/

@timing
def mat_multiply(A, B):
    """
    Matrix multiply arrays A and B

    NOTES
    np.einsum('ij, jk -> ik', A, B)
    ij are axes of A
    jk are axes of B
    ik are axes of output

    Repeating letters in input arrays i.e. j means values ALONG the axes will be multiplied
    Omitting a letter from the output means values ALONG that axis will be summed (j is not included)

    Args:
        A: <np.Array> first array
        B: <np.Array> second array

    Returns:
        <np.Array> output array

    """
    # numpy will take out labels that appeared once and arrange in alphabetical order if -> is omitted
    res = np.einsum('ij, jk -> ik', A, B)

    # check that the results are the same
    assert (res == np.einsum('ij, jk', A, B)).all()
    assert (res == A @ B).all()

    return res


A = np.array([[1, 1, 1],
              [2, 2, 2],
              [5, 5, 5]])

B = np.array([[0, 1, 0],
              [1, 1, 0],
              [1, 1, 1]])

print(mat_multiply(A, B))
