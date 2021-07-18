"""
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

4
S S S T
X X X X
X X X X
T T T X
"""

N = int(input())
graph = []
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
result = False
for i in range(N):
    graph.append(list(input().split()))


def dfs(graph, i, j):
    for direction in directions:
        n_i, n_j = i + direction[0], j + direction[1]
        while True:
            if n_i < 0 or n_j < 0 or n_i >= N or n_j >= N:
                break
            if graph[n_i][n_j] == "O":
                break
            if graph[n_i][n_j] == "S":
                return False
            n_i, n_j = n_i + direction[0], n_j + direction[1]

    return True


def solution(graph, count, start):
    # 현재 위치
    global result
    if count == 3:
        this_result = True
        for i in range(N):
            for j in range(N):
                if graph[i][j] == "T":
                    if not dfs(graph, i, j):
                        this_result = False

        if this_result:
            result = True
    else:
        for i in range(start, N*N):
            x, y = divmod(i, N)

            if graph[x][y] == "X":
                graph[x][y] = "O"
                solution(graph, count + 1, i + 1)
                graph[x][y] = "X"

    return False


solution(graph, 0, 0)
# print(result)
print("YES" if result else "NO")


