
def bfs(graph, n, visited):
    q = []
    q.append(n)
    visited[n] = True
    while q:
        num = q.pop(0)
        print(num, end=" ")
        for i in graph[num]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)