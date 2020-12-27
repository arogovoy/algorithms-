# Uses python3
import sys


# Majority Element

def count_max(a, v, l, r):
    return sum(1 for i in range(l, r + 1) if a[i] == v)


def get_majority_element(a, left, right):
    if left == right:
        return a[left]

    m = int((left + right) / 2)
    left_el = get_majority_element(a, left, m)
    right_el = get_majority_element(a, m + 1, right)

    if left_el == right_el:
        return left_el

    count_left = count_max(a, left_el, left, m)
    count_right = count_max(a, right_el, m + 1, right)

    return left_el if count_left > count_right else right_el


def majority_element_exists(a):
    n = len(a)
    el = get_majority_element(a, 0, n - 1)
    return 1 if n / 2 < count_max(a, el, 0, n - 1) else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(majority_element_exists(a))
    # print(majority_element_exists([2, 3, 3, 3, 2]))  # 1
    # print(majority_element_exists([1, 2, 3, 4]))  # 0
    # print(majority_element_exists([1, 2, 3, 1]))  # 0
