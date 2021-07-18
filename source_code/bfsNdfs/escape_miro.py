"""
5 6
101010
111111
000001
111111
111111
"""

N, M = map(int, input().split())


def bfs(graph, i, j):
    q = list()
    q.append((i, j))
    direction_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while q:
        i, j = q.pop(0)

        for direction in direction_list:
            n_i, n_j = i + direction[0], j + direction[1]

            if n_j < 0 or n_i < 0 or n_i >= N or n_j >= M:
                continue
            if graph[n_i][n_j] == 0:
                continue

            if graph[n_i][n_j] == 1:
                q.append((n_i, n_j))
                graph[n_i][n_j] = graph[i][j] + 1

    return graph


graph = []


for _ in range(N):
    graph.append(list(map(int, input())))


result_graph = bfs(graph, 0, 0)
print(result_graph[N-1][M-1])
