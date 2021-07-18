big = 0
small = 0


def binary_search(data, start, end):
    global big, small

    if start > end:
        return
    mid = (start + end) // 2

    if data[mid] >= mid:
        big += 1
        binary_search(data, mid+1, end)
    else:
        small += 1
        binary_search(data, start, mid - 1)


N = int(input())
data = list(map(int,  input().split()))

binary_search(data, 0, len(data) - 1)
print(min(big, small))