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
    res = np.tensordot(A, B, axes=1)

    assert res == A @ B

    return res


def tensor_double_contraction(A, B):
    # element-wise multiplication and then sum
    manual_res = np.multiply(A, B).sum()

    res = np.tensordot(A, B, axes=2)  # axes = 2 is also the default case

    assert res == manual_res

    return res


if __name__ == '__main__':
    # Just trying out vectors right now
    A = np.array([1, 2, 3])
    B = np.array([4, 5, 6])

    print(tensor_prod(A, B))
    print(tensor_dot_prod(A, B))

    C = np.array([[1, 2, 3],
                  [4, 2, 2],
                  [2, 3, 4]])

    D = np.array([[1, 4, 7],
                  [2, 5, 8],
                  [3, 6, 9]])

    print(tensor_double_contraction(C, D))
