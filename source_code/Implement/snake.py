
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
"""


def get_axis(now, dir):
    axis_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for idx, axis in enumerate(axis_list):
        if now == axis:
            if dir == "D":
                return axis_list[(idx + 1) % 4]
            elif dir == "L":
                return axis_list[(idx - 1) % 4]


def solution():
    N = int(input())
    snake_map = [[0] * N for _ in range(N)]

    apple_num = int(input())

    for i in range(apple_num):
        axis = list(map(int, input().split()))
        snake_map[axis[0]][axis[1]] = "a"

    timer = int(input())
    time_list = []
    for i in range(timer):
        temp = input().split()
        time_list.append((int(temp[0]), temp[1]))


    time_list.sort(key=lambda x: x[0])

    direction = (0, 1)
    time = 1
    length = 1


