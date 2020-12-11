# Uses python3
import sys


#  6 Maximum Number of Prizes


def optimal_summands(n):
    summands = []

    s = 0
    i = 1

    while s + i <= n:
        s += i
        summands.append(i)
        i += 1

    if s < n:
        summands.append(n - s + summands.pop())

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
