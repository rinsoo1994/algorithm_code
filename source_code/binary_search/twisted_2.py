from bisect import bisect_left
from bisect import bisect_right
from bisect import bisect


def binary_search(data, start, end):
    global big, small

    if start > end:
        return
    mid = (start + end) // 2
    # print(data[mid])
    # 인덱스보다 해당 값이 클때
    if data[mid] >= mid:

        min_index = bisect_right(data, data[mid])
        # print(this_index)
    # 인덱스보다 해당 값이 작을때
    else:



N = int(input())
data = list(map(int,  input().split()))

binary_search(data, 0, len(data) - 1)
