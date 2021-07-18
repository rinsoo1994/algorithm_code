"""
Q.28 고정점 찾기

5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
"""
import math


def find_point(data, start_point, mid_point, end_point):
    global result

    if data[mid_point] == mid_point:
        return mid_point

    elif start_point == mid_point or mid_point == end_point:
        return -1

    elif data[mid_point] > mid_point:
        temp = mid_point
        mid_point = start_point + math.floor((mid_point - start_point)/2)
        end_point = temp
        return find_point(data, start_point, mid_point, end_point)

    elif data[mid_point] < mid_point:
        temp = mid_point
        mid_point = mid_point + math.floor((end_point - mid_point) / 2)
        start_point = temp
        return find_point(data, start_point, mid_point, end_point)


N = int(input())
data = list(map(int, input().split()))
mid_point = math.floor(len(data)/2)
result = find_point(data, 0, mid_point, N-1)
print(result)
