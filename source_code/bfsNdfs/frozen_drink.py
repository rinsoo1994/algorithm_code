"""
4 5
00110
00011
11111
00000
"""


N, M = map(int, input().split())

graph = []


def dfs(graph, i, j):
    if i < 0 or j < 0 or i >= N or j >= M:
        return False

    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(graph, i + 1, j)
        dfs(graph, i, j + 1)
        dfs(graph, i - 1, j)
        dfs(graph, i, j - 1)
        return True

    return False


for i in range(N):
    graph.append(list(map(int, input())))

count = 0
for i in range(N):
    for j in range(M):
        result = dfs(graph, i, j)
        if result:
            count += 1

print(count)