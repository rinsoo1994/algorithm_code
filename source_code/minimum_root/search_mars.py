"""
Q36. 화성탐사

3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""

import heapq


iter_num = int(input())

"""
5 5 4
3 9 1
3 2 7
"""


for num in range(iter_num):
    N = int(input())
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # 공간 초기화
    space = []
    for i in range(N):
        row_data = list(map(int, input().split()))
        space.append(row_data)

    # 방문초기화
    sum_visited = [[10e9 for _ in range(N)] for _ in range(N)]

    sum_visited[0][0] = space[0][0]
    q = [(space[0][0], 0, 0)]

    while q:
        dist, x, y = heapq.heappop(q)
        if sum_visited[x][y] < dist:
            continue

        for direction in directions:
            n_x = direction[0] + x
            n_y = direction[1] + y

            if n_x < 0 or n_y < 0 or n_x >= N or n_y >= N:
                continue

            cost = dist + space[n_x][n_y]
            if cost < sum_visited[n_x][n_y]:
                sum_visited[n_x][n_y] = cost
                heapq.heappush(q, (cost, n_x, n_y))

    # visit(sum_visited, space)

    print(sum_visited[N-1][N-1])
