"""
Q.39

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

INF = 1e9
DIRECTION = [(1, 0), (0, 1), (-1, 0), (0, -1)]


T = int(input())
for _ in range(T):
    N = int(input())
    graph = []
    distance = [[INF] * N for _ in range(N)]

    for i in range(N):
        graph.append(list(map(int, input().split())))

    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:
        cost, a, b = heapq.heappop(q)
        for direction in DIRECTION:
            n_a, n_b = a + direction[0], b + direction[1]
            if (0 <= n_a < N) and(0 <= n_b < N):
                n_cost = cost + graph[n_a][n_b]
                if distance[n_a][n_b] > n_cost:
                    heapq.heappush(q, (n_cost, n_a, n_b))
                    distance[n_a][n_b] = n_cost

    print(distance[N-1][N-1])