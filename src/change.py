# Uses python3
import sys


# Task. The goal in this problem is to find the minimum number of coins needed to change
#   the input value (an integer) into coins with denominations 1, 5, and 10.
# Input Format. The input consists of a single integer 𝑚.
# Constraints. 1 ≤ 𝑚 ≤ 10^3.
# Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.
# Sample 2.
# Input: 28
# Output: 6
# 28 = 10 + 10 + 5 + 1 + 1 + 1.

def get_change(m: int):
    coins = [10, 5, 1]
    res = 0
    i = 0
    while m and i < len(coins):
        c = int(m / coins[i])
        if c > 0:
            res += c
        m -= coins[i] * c
        i += 1
    return res


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    # print(get_change(28), 6)
    # print(get_change(2), 2)
    # print(get_change(1000), 100)
    # print(get_change(43), 7)
