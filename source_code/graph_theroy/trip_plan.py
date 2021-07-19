"""
Q 41. 여행 계획

5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3

"""

M, N = map(int, input().split())

graph = {}
for num in range(M):
    idx = num + 1
    graph[idx] = [d_idx + 1 for d_idx, data in enumerate(list(map(int, input().split()))) if data == 1]

print(graph)
trip_plan = list(map(int, input().split()))

result = "YES"

for idx in range(N-1):

    now_p = trip_plan[idx]
    next_p = trip_plan[idx + 1]
    print("현재, 다음", now_p, next_p)
    if next_p in graph[now_p]:
        print("있음")
        continue
    else:
        result = "NO"
        for data in graph[now_p]:
            print(data)
            if next_p in graph[data]:
                result = "YES"
                break


print(result)
# print(now_p, next_p)
