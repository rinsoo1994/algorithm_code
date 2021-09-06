"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())
graph = [[] for i in range(n + 1)]
# visited = [False] * (n + 1)

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print("graph", graph)


def dijkstra(start):
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, node = heapq.heappop(q)
        if distance[node] < cost:
            continue
        for related in graph[node]:
            # 거리가 지금 거리 그래프 보다 작으면 거리 갱신, heappush
            if distance[related[0]] > related[1] + cost:
                distance[related[0]] = related[1] + cost
                heapq.heappush(q, (related[1] + cost, related[0]))


dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
