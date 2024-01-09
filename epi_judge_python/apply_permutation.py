from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    for ix in range(len(A)):
        if perm[ix] >= 0:
            perm_ix = perm[ix]
            while perm_ix != ix:
                A[perm_ix], A[ix] = A[ix], A[perm_ix]
                perm[perm_ix] -= len(perm)
                perm_ix = perm[perm_ix] + len(perm)
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
