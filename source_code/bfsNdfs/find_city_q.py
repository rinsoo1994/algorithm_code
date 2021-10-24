"""
4 4 2 1
1 2
1 3
2 3
2 4


4 3 2 1
1 2
1 3
1 4


4 4 1 1
1 2
1 3
2 3
2 4
"""
import sys
input = sys.stdin.readline
from collections import deque
N, M, K, X = map(int, input().split(" "))
road_dict = {}
for _ in range(M):
    a, b = map(int, input().split())
    if a not in road_dict:
        road_dict[a] = []
    road_dict[a].append(b)

init_distance = {i: 1e8 for i in range(1, N+1)}

visited = deque([X])
init_distance[X] = 0


while visited:
    temp = visited.popleft()
    if temp in road_dict:
        for i in road_dict[temp]:
            if init_distance[i] == 1e8:
                init_distance[i] = init_distance[temp] + 1
                visited.append(i)

result = []
for k, v in init_distance.items():
    if v == K:
        result.append(k)

if not result:
    result = -1
    print(result)
else:
    for r in result:
        print(r)

