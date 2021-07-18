"""
2 20 50
50 30
20 40

2 40 50
50 30
20 40

2 20 50
50 30
30 40

"""
N, L, R = map(int, input().split())

graph = []
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
result_count = 10e9
for _ in range(N):
    graph.append(list(map(int, input().split())))


def solution(graph, s_i, s_j, count):
    global result_count
    for i in range(s_i, N):
        for j in range(s_j, N):
            for direction in directions:
                n_i, n_j = i + direction[0], j + direction[1]

                if n_i < 0 or n_j < 0 or n_i >= N or n_j >= N:
                    continue

                diff = abs(graph[i][j] - graph[n_i][n_j])
                if diff >= L and diff <= R:
                    i_j = graph[i][j]
                    n_i_j = graph[n_i][n_j]

                    mid_value = int((i_j + n_i_j)/2)
                    graph[i][j], graph[n_i][n_j] = mid_value, mid_value

                    count = solution(graph, i, j, count+1)
                    graph[i][j], graph[n_i][n_j] = i_j, n_i_j

    result_count = min(result_count, count)
    return count


solution(graph, 0, 0, 0)


if result_count == 10e9:
    result_count = 0
print(result_count)
