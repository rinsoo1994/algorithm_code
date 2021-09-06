"""
Q.40

6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""

import heapq

INF = 1e9
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(M):
    q = []
    distance[1] = 0
    heapq.heappush(q, (0, 1))

    while q:
        dist, x = heapq.heappop(q)
        cost = dist + 1
        for n in graph[x]:
            if distance[n] > cost:
                distance[n] = cost
                heapq.heappush(q, (cost, n))

for idx, d in enumerate(distance):
    if d == INF:
        distance[idx] = 0


print(distance.index(max(distance)), end=" ")
print(max(distance), end=" ")
print(distance.count(max(distance)))
