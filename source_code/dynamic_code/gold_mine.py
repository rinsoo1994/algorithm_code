"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
[[1, 3, 3, 2],
 [2, 1, 4, 1],
 [0, 6, 4, 7]]

[[1, 5, 4, 6],
 [2, 1, 5, 5],
 [0, 6, 5, 12]]


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    init_list = [[0] * m for _ in range(n)]

    input_numbers = list(map(int, input().split()))
    for nn in range(n):
        for mm in range(m):
            init_list[nn][mm] = input_numbers[nn*m + mm]

    allow_direction = [(0, 1), (1, 1), (-1, 1)]

    queue = []
    for i in range(n):
        queue.append([i, 0])

    while queue:
        x, y = queue.pop(0)
        for i in range(m):
            for allow in allow_direction:
                n_x, n_y = x + allow[0], y + allow[1]

                if n_x < 0 or n_y < 0 or n_x >= n or n_y >= m:
                    continue

                if init_list[x][y] + init_list[n_x][n_y] >= init_list[x][y]:
                    queue.append((n_x, n_y))
                    init_list[n_x][n_y] = init_list[x][y] + init_list[n_x][n_y]

    print(init_list)
    result = 0
    for num in range(n):
        result = max(result, init_list[num][m-1])
    print(result)