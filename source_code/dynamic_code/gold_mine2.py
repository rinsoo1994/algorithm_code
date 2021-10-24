"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
from collections import deque

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    mining = [[0] * m for _ in range(n)]

    inputs = list(map(int, input().split()))

    for a in range(n):
        for b in range(m):
            graph[a][b] = inputs[a * m + b]
            mining[a][b] = inputs[a * m + b]

    allow_direction = [(0, 1), (1, 1), (-1, 1)]

    queue = deque()
    for i in range(n):
        queue.append([i, 0])

    while queue:
        x, y = queue.popleft()

        for i in range(m):
            for allow in allow_direction:
                n_x, n_y = x + allow[0], y + allow[1]

                if n_x < 0 or n_y < 0 or n_x >= n or n_y >= m:
                    continue

                if mining[x][y] + graph[n_x][n_y] >= mining[n_x][n_y]:
                    if (n_x, n_y) not in queue:
                        queue.append((n_x, n_y))
                    mining[n_x][n_y] = mining[x][y] + graph[n_x][n_y]

    result = max([mining[num][m - 1] for num in range(n)])
    print(result)
