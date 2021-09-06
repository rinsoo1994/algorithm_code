"""
3 2 1
1 2 4
1 3 2
"""
import heapq
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)


for _ in range(m):
    d, e, f = map(int, input().split())
    graph[d].append((e, f))

print(distance)
print(graph)


def daijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dis, now = heapq.heappop(q)
        for info in graph[now]:
            cost = dis + info[1]
            if distance[info[0]] > cost:
                distance[info[0]] = cost
                heapq.heappush(q, (cost, info[0]))


daijkstra(c)

count = 0
max = 0
for d in distance:
    if d == INF:
        continue
    else:
        count += 1
    if d > max:
        max = d
