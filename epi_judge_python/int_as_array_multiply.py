from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    result = [0] * (len(num1) + len(num2))
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    num1.reverse()
    num2.reverse()

    for ix1, val1 in enumerate(num1):
        for ix2, val2 in enumerate(num2):
            result[ix1 + ix2] += val1 * val2
            result[ix1 + ix2 + 1] += result[ix1 + ix2] // 10
            result[ix1 + ix2] %= 10
    
    result.reverse()

    result = result[next((ix for ix, val in enumerate(result) if val != 0),
                         len(result)):] or [0]

    result = [sign * result[0]] + result[1:]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
