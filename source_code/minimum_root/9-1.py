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

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print("graph", graph)


# 방문하지 않은 노드들 중에서 가장 최단거리가 짧은 노드 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]
    print("distance", distance)

    # 시작 노드 제외한 n-1개의 노드에서 반복?
    for i in range(n-1):
        now = get_smallest_node()
        print("now", now)
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
