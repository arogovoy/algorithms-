# Uses python3

import sys


# Maximum Salary

def decreaseValue(a):
    while a / 10 >= 1:
        a /= 10
    return a


def sort(arr):
    pseudo = list(map(decreaseValue, arr))
    i = 1
    while i < len(pseudo):
        j = i - 1
        p = pseudo[i]
        a = arr[i]
        while j >= 0 and p > pseudo[j]:
            pseudo[j + 1] = pseudo[j]
            arr[j + 1] = arr[j]
            j -= 1
        pseudo[j + 1] = p
        arr[j + 1] = a
        i += 1
    return arr


def largest_number(a):
    a = sort(a)

    return a


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = input.split()
    # a = data[1:]
    print(largest_number([23, 39, 92, 9, 3, 357, 359, 368, 335, 9, 900]))  # 9 92 39 368 359 357 335 3 23
