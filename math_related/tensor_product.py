import numpy as np


def tensor_prod(A, B):
    res_arr = []

    for A_elem in A:
        for B_elem in B:
            res_arr.append(A_elem * B_elem)

    res = np.tensordot(A, B, axes=0)  # axes = 0 for tensor product
    res = res.reshape(res.size)

    assert (np.array(res_arr) == res).all()
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
