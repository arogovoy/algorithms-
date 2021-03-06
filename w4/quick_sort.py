# Uses python3
import sys
import random


# Improving Quick Sort

def partition3(a, l, r):
    x = a[l]
    j = l
    xs, xe = -1, -1
    for i in range(l + 1, r + 1):
        if a[i] < x:
            if xs != -1:
                a[xs], a[xe + 1] = a[xe + 1], a[xs]
                if a[xs] > x:
                    a[xs], a[i] = a[i], a[xs]
                xs += 1
                xe += 1
            else:
                j += 1
                a[i], a[j] = a[j], a[i]

        elif a[i] == x:
            if xs == -1:
                j += 1
                a[i], a[j] = a[j], a[i]
                xs, xe = j, j
            else:
                xe += 1
                a[xe], a[i] = a[i], a[xe]

    if xs == -1:
        a[l], a[j] = a[j], a[l]
        xs, xe = j, j
    else:
        xs -= 1
        a[xs], a[l] = a[l], a[xs]

    return xs, xe


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    xs, xe = partition3(a, l, r)
    randomized_quick_sort(a, l, xs - 1)
    randomized_quick_sort(a, xe + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
