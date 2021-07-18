from itertools import combinations
"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""
"""
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
"""

"""
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
"""
N, M = map(int, input().split())
candidates = list(combinations([num for num in range(N*M)], 3))
origin_list = []


def dfs(graph, i, j):
    if i < 0 or j < 0 or i >= N or j >= M:
        return
    if graph[i][j] == 1:
        return
    if graph[i][j] == -2:
        return
    if graph[i][j] == 2:
        origin_list.append((i, j))

    graph[i][j] = -2

    dfs(graph, i+1, j)
    dfs(graph, i, j + 1)
    dfs(graph, i - 1, j)
    dfs(graph, i, j - 1)
    return


graph = []
for n1 in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

safe_zone = 0
for candidate in candidates:
    x1, y1 = divmod(candidate[0], M)
    x2, y2 = divmod(candidate[1], M)
    x3, y3 = divmod(candidate[2], M)

    if graph[x1][y1] == 1 or graph[x1][y1] == 2:
        continue
    elif graph[x2][y2] == 1 or graph[x2][y2] == 2:
        continue
    elif graph[x3][y3] == 1 or graph[x3][y3] == 2:
        continue

    graph[x1][y1] = 1
    graph[x2][y2] = 1
    graph[x3][y3] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                dfs(graph, i, j)

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                count += 1
            elif graph[i][j] == -2:
                graph[i][j] = 0
    for origin in origin_list:
        graph[origin[0]][origin[1]] = 2

    safe_zone = max(safe_zone, count)

    graph[x1][y1] = 0
    graph[x2][y2] = 0
    graph[x3][y3] = 0

print(safe_zone)