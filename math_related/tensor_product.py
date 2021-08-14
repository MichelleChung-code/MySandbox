import numpy as np


def tensor_prod(A, B):
    # https://www.math3ma.com/blog/the-tensor-product-demystified
    manual_arr = []

    for A_elem in A:
        for B_elem in B:
            manual_arr.append(A_elem * B_elem)

    # Technically also called the outer product
    outer_arr_np = np.outer(A, B)

    res = np.tensordot(A, B, axes=0)  # axes = 0 for tensor product

    res_arr = np.array(manual_arr).reshape(res.shape)  # matrix-vector duality

    assert np.logical_and((res_arr == outer_arr_np).all(), (res == res_arr).all())
    return res


def tensor_dot_prod(A, B):
    # add code for the assertation
    res = np.tensordot(A, B, axes=1)
    return res


def tensor_double_contraction(A, B):
    # add code for assertation
    res = np.tensordot(A, B, axes=2)  # axes = 2 is also the default case
    return res


if __name__ == '__main__':
    # Just trying out vectors right now
    A = np.array([1, 2, 3])
    B = np.array([4, 5])

    print(tensor_prod(A, B))
