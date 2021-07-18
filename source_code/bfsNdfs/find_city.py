"""
4 4 2 1
1 2
1 3
2 3
2 4
"""
"""
10 3 2 1
1 2
1 3
1 4
"""
"""
10 4 1 1
1 2
1 3
2 3
2 4
"""

from collections import deque

N, M, K, X = map(int, input().split())

graph = [[]for _ in range(N+1)]
distance = [-1 for _ in range(N+1)]

for _ in range(M):
    data = list(map(int, input().split()))
    graph[data[0]].append(data[1])

q = deque([X])
distance[X] = 0
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for idx, d in enumerate(distance):
    if d == K:
        check = True
        print(idx)

if not check:
    print(-1)

