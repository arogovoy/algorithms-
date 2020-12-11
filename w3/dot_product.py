# Task. Given two sequences 𝑎1,𝑎2,...,𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1,𝑏2,...,𝑏𝑛
#   (𝑏𝑖 is the average number of clicks per day of the 𝑖-th slot), we need to partition them into 𝑛 pairs (𝑎𝑖,𝑏𝑗)
#   such that the sum of their products is maximized.
# Input Format. The first line contains an integer 𝑛, the second one contains a sequence of integers 𝑎1,𝑎2,...,𝑎𝑛,
#   the third one contains a sequence of integers 𝑏1,𝑏2,...,𝑏𝑛.
# Constraints. 1≤𝑛≤10^3;−10^5 ≤𝑎𝑖,𝑏𝑖 ≤10^5 for all 1≤𝑖≤𝑛.
# 𝑛
# Output Format. Output the maximum value of ∑︀ 𝑎𝑖𝑐𝑖, where 𝑐1, 𝑐2, . . . , 𝑐𝑛 is a permutation of
#  𝑏1,𝑏2,...,𝑏𝑛.

import sys


def sort(arr):
    i = 1
    while i < len(arr):
        j = i - 1
        v = arr[i]
        while j >= 0 and v < arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = v
            j -= 1

        arr[j + 1] = v
        i += 1
    return arr


def max_dot_product(a, b):
    a = sort(a)
    b = sort(b)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

    # print(max_dot_product([23], [39]), 897)
    # print(max_dot_product([1, 3, -5], [-2, 4, 1]), 23)
