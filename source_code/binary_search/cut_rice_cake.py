"""
4 6
19 15 10 17
"""


def minus_cake_length_sum(cutting, array):
    return sum([arr - cutting for arr in array if arr >= cutting])


def binary_search(array, find_num, start, end):
    while start <= end:
        target = (start + end) // 2
        if minus_cake_length_sum(target, array) == find_num:
           return target
        elif minus_cake_length_sum(target, array) < find_num:
           end = target - 1
        else:
           start = target + 1
    return None


N, M = map(int, input().split())
input_arr = list(map(int, input().split()))
result = binary_search(input_arr, 6, 0, max(input_arr))
print(result)