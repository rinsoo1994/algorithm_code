# def change_index(idx, k, arr, lenth, count):
#     check = True
#     for i, d in enumerate(arr):
#         if i + 1 == d:
#             continue
#         else:
#             check = False
#     if check:
#         return
#
#     for num in range(k, 0, -1):
#         n_idx = idx + num
#         if idx - num >= 0:
#             if arr[n_idx] == n_idx + 1:
#                 continue
#             else:
#                 temp = arr[idx]
#                 arr[idx] = arr[n_idx]
#                 arr[n_idx] = temp
#                 change_index(idx, k, arr, lenth, count+1)
#
#
#     pass
import copy
min_count = 10e10


def change_index(arr, k, count):
    check = True

    for i, d in enumerate(arr):
        if i == 0:
            continue
        if i  == d:
            continue
        else:
            check = False

    global min_count
    if check:

        min_count = min(min_count, count)
        return

    for idx, arr_data in enumerate(arr):
        if idx == 0:
            continue
        if idx == arr_data:
            continue
        down_limit = idx - k
        up_limit = idx + k

        if down_limit < 0:
            down_limit = 0

        if up_limit >= len(arr):
            up_limit = len(arr) - 1

        if down_limit <= arr_data <= up_limit:
            tmp = arr[arr_data]
            copy_arr = copy.deepcopy(arr)
            copy_arr[arr_data] = arr_data
            copy_arr[idx] = tmp
            print(copy_arr)
            change_index(copy_arr, k, count + 1)


def solution(arr, k):
    arr.insert(0, 0)
    change_index(arr, k, 0)
    global min_count
    return min_count


solution([5, 4, 3, 2, 1], 2)
print(min_count)