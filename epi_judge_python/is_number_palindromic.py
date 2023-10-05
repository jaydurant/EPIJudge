from test_framework import generic_test
import math

def is_palindrome_number(x: int) -> bool:
    if x <= 0:
        return x == 0

    x_len = math.floor(math.log10(x)) + 1

    mask = 10 ** (x_len - 1)

    for _ in range(x_len // 2):
        msd = x // mask
        lsd = x % 10
        if msd != lsd:
            return False
        
        x %= mask
        x //= 10
        mask //= 100

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
