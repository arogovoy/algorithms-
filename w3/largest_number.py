# Uses python3

import sys
from math import log, pow
from functools import reduce


# Maximum Salary

def compare(a, b):
    order_a = int(log(a, 10))
    order_b = int(log(b, 10))

    num1 = a * pow(10, order_b + 1) + b
    num2 = b * pow(10, order_a + 1) + a

    return num2 < num1


def largest_number(arr):
    i = 1
    while i < len(arr):
        j = i - 1
        a = arr[i]
        while j >= 0 and compare(int(a), int(arr[j])):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = a
        i += 1

    return int(reduce(lambda v1, v2: str(v1) + str(v2), arr))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    # print(largest_number([23, 39, 92, 9, 3, 357, 359, 368, 335, 9, 900]))  # 9 9 92 39 368 359 357 335 3 23
    # print(largest_number([23, 39, 92]))  # 923923
