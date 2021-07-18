
"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

"""

from heapq import heappush, heappop
inf = 10e9
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
dp = [inf] * (V + 1)
heap = []


def distra(start):
    dp[start] = 0
    heappush(heap, [0, start])

    while heap:
        dist, now = heappop(heap)

        if dp[now] < dist:
            continue

        # 연결되있는 노드 가져오기
        for node in graph[now]:
            cost = dist + node[1]

            if cost < dp[node[0]]:
                dp[node[0]] = cost
                heappush(heap, (cost, node[0]))


for num in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


distra(K)


for i in range(1, V+1):
    if dp[i] == inf:
        print("INF")
    else:
        print(dp[i])



