import numpy as np
def _print_big_matrix(mat):
    for row in mat:
        for elem in row:
            elem = np.real_if_close(np.round(elem, 3), tol=1e-1)
            if not np.isclose(elem, 0., atol=1e-2):
                print(f'{elem:.1f}', end=' ')
            else:
                print(' . ', end=' ')
        print()