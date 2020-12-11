# -*- coding: utf-8 -*-

import sys


# Car Fueling
# Problem Introduction
# You are going to travel to another city that is located 𝑑 miles away from your home city.
# Your car can travel at most 𝑚 miles on a full tank and you start with a full tank.
# Along your way, there are gas stations at distances stop1, stop2, . . . , stop𝑛 from your home city.
# What is the minimum number of refills needed?
# Problem Description
# Input Format. The first line contains an integer 𝑑. The second line contains an integer 𝑚.
#   The third line specifies an integer 𝑛. Finally, the last line contains integers stop1, stop2, . . . , stop𝑛.
# Output Format. Assuming that the distance between the cities is 𝑑 miles,
#   a car can travel at most 𝑚 miles on a full tank, and there are gas stations at distances
#   stop1 , stop2 , . . . , stop𝑛 along the way, output the minimum number of refills needed.
#   Assume that the car starts with a full tank. If it is not possible to reach the destination, output −1.
# Constraints. 1≤𝑑≤10^5.1≤𝑚≤400.1≤𝑛≤300.0<stop1 <stop2 <···<stop𝑛 <𝑑.
# Sample 1.
# Input:
# 950
# 400
# 4
# 200 375 550 750
# Output: 2

def compute_min_refills(distance, tank, stops):
    prev = 0
    refills = 0
    s = 0

    stops.append(distance)

    while s < len(stops):
        cur = tank
        while cur >= 0 and s < len(stops):
            cur += prev - stops[s]

            if cur >= 0:
                prev = stops[s]
                s += 1
            elif stops[s] - prev > tank:
                return -1
            else:
                refills += 1

    return refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
    # print(compute_min_refills(950, 400, [200, 375, 550, 750]))  # 2
    # print(compute_min_refills(10, 3, [1, 2, 5, 9]))  # -1
    # print(compute_min_refills(200, 250, [100, 150]))  # 0
    # print(compute_min_refills(10, 2, [1, 3, 4, 5, 7, 9]))  # 5
    # print(compute_min_refills(10, 2, [1]))  # -1
    # print(compute_min_refills(10, 2, [9]))  # -1
    # print(compute_min_refills(10, 9, [9]))  # 1
    # print(compute_min_refills(10, 20, [1, 2, 3, 4, 5]))  # 0
