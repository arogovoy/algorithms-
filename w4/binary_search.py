# Uses python3
import sys

# Binary Search

def sub_search(a, l, r, x):
    m = int((l + r) / 2)
    if l >= r:
        return -1

    if a[m] == x:
        return m
    return sub_search(a, l, m, x) if a[m] > x else sub_search(a, m + 1, r, x)


def binary_search_recursive(a, x):
    return sub_search(a, 0, len(a), x)


def binary_search_linear(a, x):
    l, r = 0, len(a)
    while l < r:
        m = int((l + r) / 2)
        if a[m] == x:
            return m
        if a[m] > x:
            r = m
        else:
            l = m + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search_linear(a, x), end = ' ')
