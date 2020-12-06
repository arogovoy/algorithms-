# Uses python3
import sys


# Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
# Input Format. The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
#   The next 𝑛 lines define the values and weights of the items.
#   The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the value and the weight of 𝑖-th item, respectively.
# Constraints. 1≤𝑛≤10^3,0≤𝑊 ≤2·10^6;0≤𝑣𝑖 ≤2·10^6,0<𝑤𝑖 ≤2·10^6 for all 1≤𝑖≤𝑛. All the numbers are integers.
# Output Format. Output the maximal value of fractions of items that fit into the knapsack.
#   The absolute value of the difference between the answer of your program and the optimal value should be at most 10−3
#   To ensure this, output your answer with at least four digits after the decimal point
#   (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).
# Sample 1.
# Input:
# 3 50
# 60 20
# 100 50
# 120 30
# Output:
# 180.0000
# To achieve the value 180, we take the first item and the third item into the bag.

def sort(values, weights):
    i = 1
    while i < len(values):
        j = i - 1
        v = values[i]
        w = weights[i]
        while j >= 0 and (v / w) > (values[j] / weights[j]):
            values[j + 1] = values[j]
            weights[j + 1] = weights[j]
            j -= 1
        values[j + 1] = v
        weights[j + 1] = w
        i += 1
    return values, weights


def get_optimal_value(capacity, weights, values):
    values, weights = sort(values, weights)
    value = 0.
    i = 0
    while capacity >= 0 and i < len(weights):
        capacity -= weights[i]
        if capacity < 0:  # overweight
            value += (weights[i] + capacity) * values[i] / weights[i]
        else:
            value += values[i]
        i += 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))

    # opt_value = get_optimal_value(50, [20, 50, 30], [60, 100, 120])
    # print("{:.4f}".format(opt_value))
    # opt_value = get_optimal_value(10, [30], [500])
    # print("{:.4f}".format(opt_value))

