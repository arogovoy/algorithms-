# Uses python3
import sys
from collections import namedtuple

# 3.5 Collecting Signatures

Segment = namedtuple('Segment', 'start end')


def sort(segments):
    i = 0
    while i < len(segments):
        j = i - 1
        seg = segments[i]
        while j >= 0 and seg.start < segments[j].start:
            segments[j + 1] = segments[j]
            segments[j] = seg
            j -= 1
        segments[j + 1] = seg
        i += 1
    return segments


def optimal_points(segments):
    segments = sort(segments)
    points = []

    i = 0

    while i < len(segments):
        seg = segments[i]
        common_point = seg.end
        i += 1
        while i < len(segments) and common_point >= segments[i].start:
            common_point = segments[i].end if common_point > segments[i].end else common_point
            i += 1

        points.append(common_point)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

    # segments = list(map(lambda x: Segment(x[0], x[1]), [[3, 6], [2, 5], [1, 3]]))
    # points = optimal_points(segments)
    # print(len(points))
    # print(*points)
    #
    # print('------')
    #
    # segments = list(map(lambda x: Segment(x[0], x[1]), [[4, 7], [1, 3], [2, 5], [5, 6]]))
    # points = optimal_points(segments)
    # print(len(points))
    # print(*points)
    #
    # print('------')
    #
    # segments = list(map(lambda x: Segment(x[0], x[1]), [[0, 1000000000]]))
    # points = optimal_points(segments)
    # print(len(points))
    # print(*points)
    #
    # print('------')
    #
    # segments = list(map(lambda x: Segment(x[0], x[1]), [[0, 10], [10, 11]]))
    # points = optimal_points(segments)
    # print(len(points))
    # print(*points)
    #
    # print('------')
    #
    # segments = list(map(lambda x: Segment(x[0], x[1]), [[0, 10], [11, 12]]))
    # points = optimal_points(segments)
    # print(len(points))
    # print(*points)

    # # print('------')
    #
    # a = [41, 42, 52, 52, 63, 63, 80, 82, 78, 79, 35, 35, 22, 23, 31, 32, 44, 45, 81, 82, 36, 38, 10, 12, 1, 1, 23, 23,
    #      32, 33, 87, 88, 55, 56, 69, 71, 89, 91, 93, 93, 38, 40, 33, 34, 14, 16, 57, 59, 70, 72, 36, 36, 29, 29, 73, 74,
    #      66, 68, 36, 38, 1, 3, 49, 50, 68, 70, 26, 28, 30, 30, 1, 2, 64, 65, 57, 58, 58, 58, 51, 53, 41, 41, 17, 18, 45,
    #      46, 4, 4, 0, 1, 65, 67, 92, 93, 84, 85, 75, 77, 39, 41, 15, 15, 29, 31, 83, 84, 12, 14, 91, 93, 83, 84, 81, 81,
    #      3, 4, 66, 67, 8, 8, 17, 19, 86, 87, 44, 44, 34, 34, 74, 74, 94, 95, 79, 81, 29, 29, 60, 61, 58, 59, 62, 62, 54,
    #      56, 58, 58, 79, 79, 89, 91, 40, 42, 2, 4, 12, 14, 5, 5, 28, 28, 35, 36, 7, 8, 82, 84, 49, 51, 2, 4, 57, 59, 25,
    #      27, 52, 53, 48, 49, 9, 9, 10, 10, 78, 78, 26, 26, 83, 84, 22, 24, 86, 87, 52, 54, 49, 51, 63, 64, 54, 54]
    #
    # segments = list(map(lambda x: Segment(x[0], x[1]), zip(a[::2], a[1::2])))
    # points = optimal_points(segments)
    # print(len(points))
    # print(*points)
