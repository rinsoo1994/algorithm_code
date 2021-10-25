"""
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
"""
N = int(input())
fixed_list = list(map(int, input().split(" ")))


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if mid == array[mid]:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1


result = binary_search(fixed_list, 0, N-1)
print(result)