"""
5 3
1
2
8
4
9
"""
N, C = map(int, input().split())
house = []
# answer
for num in range(N):
    house.append(int(input()))
house.sort()


def count_available(distance):
    s = house[0]
    count = 1
    for i in range(1, N):
        if s + distance <= house[i]:
            count += 1
            s = house[i]
    return count


start, end = 1, house[-1] - house[0]
while start <= end:
    mid = (end + start) // 2
    print(mid)
    if count_available(mid) >= C:
        answer = mid
        start = mid + 1
        print("start", start)
    else:
        end = mid - 1
        print("end", end)

print(answer)

# while start <= end:  # 이분탐색 알고리즘
#     mid = (start + end) // 2
#
#     if router_counter(mid) >= C:
#         answer = mid
#         start = mid + 1
#     else:
#         end = mid - 1