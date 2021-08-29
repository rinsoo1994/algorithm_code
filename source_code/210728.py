from copy import deepcopy
def solution(rows, columns, queries):
    graph = [[0] * (columns+1) for _ in range(rows + 1)]
    num = 1
    for y in range(columns + 1):
        for x in range(rows + 1):
            if x == 0:
                continue
            elif y == 0:
                continue
            graph[y][x] = num
            num += 1
    graph_copy = deepcopy(graph)

    # print(graph)
    answer = []
    for query in queries:
        min_num = 10e9
        y1, x1, y2, x2 = query[0], query[1], query[2], query[3]

        n_x, n_y = x1, y1

        while n_x != x2:
            print(n_x, n_y)
            graph_copy[n_x+1][n_y] = graph[n_x][n_y]
            n_x += 1
        n_x -= 1

        while n_y != y2:
            print(n_x, n_y)

            graph_copy[n_x][n_y+1] = graph[n_x][n_y]
            n_y += 1
        n_y -= 1

        print(graph_copy)
        answer.append(min_num)

    print(answer)
    return answer

solution(6, 6, [[2,2,5,4]])