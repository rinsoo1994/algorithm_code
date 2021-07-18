def change_index(idx, k, arr, lenth, count):
    check = True
    for i, d in enumerate(arr):
        if i + 1 == d:
            continue
        else:
            check = False
    if check:
        return

    for num in range(k, 0, -1):
        n_idx = idx + num
        if idx - num >= 0:
            if arr[n_idx] == n_idx + 1:
                continue
            else:
                temp = arr[idx]
                arr[idx] = arr[n_idx]
                arr[n_idx] = temp
                change_index(idx, k, arr, lenth, count+1)


    pass


def solution(arr, k):
    for idx in range(len(arr)-1, -1, -1):
        change_index(idx, k, arr, len(arr), 0)

    answer = 0
    return answer


solution([4,5,2,3,1], 2)