from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    result_arr = [0] * (len(num1) + len(num2))
     
    is_negative = False
    if num1[0] * num2[0] < 0:
        is_negative = True
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    num1.reverse()
    num2.reverse()
    for ix1, val1 in enumerate(num1):
        for ix2, val2 in enumerate(num2):
            curr_ix = ix1 + ix2
            prod = val1 * val2 + result_arr[curr_ix]
            carry = prod // 10
            lsd = prod % 10

            result_arr[curr_ix] = lsd
            result_arr[curr_ix + 1] += carry

    while result_arr[-1] == 0 and len(result_arr) > 1:
        result_arr.pop()

    if is_negative:
        result_arr[-1] *= -1
    result_arr.reverse()

    return result_arr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
