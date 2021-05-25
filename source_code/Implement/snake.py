
"""
6
3
2 4
2 5
5 3
3
3 D
15 L
17 D

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
"""


def get_axis(now, dir):
    axis_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for idx, axis in enumerate(axis_list):
        if now == axis:
            if dir == "D":
                if idx + 1 > 3:
                    return axis_list[0]
                else:
                    return axis_list[idx + 1]

            elif dir == "L":
                if idx - 1 < 0:
                    return axis_list[3]
                else:
                    return axis_list[idx - 1]


def solution():
    N = int(input())
    map_list = [[0] * N for _ in range(N)]
    apple_num = int(input())

    # map 에 apple 위치 표시
    for i in range(apple_num):
        axis = list(map(int, input().split()))

        map_list[axis[0]-1][axis[1]-1] = 2

    # timer
    timer = int(input())
    time_list = []
    for i in range(timer):
        temp = input().split()
        time_list.append((int(temp[0]), temp[1]))
    time_list.sort(key=lambda x: x[0])

    i, j = 0, 0
    snake_list = [(i, j)]
    direction = (0, 1)
    time = 0

    while True:
        i, j = i + direction[0], j + direction[1]
        if i < 0 or j < 0 or i >= N or j >= N:
            return time + 1

        if map_list[i][j] == 2:
            map_list[i][j] = 1
            snake_list.append((i, j))

        elif map_list[i][j] == 1:
            return time + 1

        else:
            snake_list.append((i, j))
            d_i, d_j = snake_list.pop(0)
            map_list[d_i][d_j] = 0

        map_list[i][j] = 1
        time += 1
        if len(time_list) >= 1 and time_list[0][0] == time:
            direction = get_axis(direction, time_list[0][1])
            time_list.pop(0)


print(solution())
