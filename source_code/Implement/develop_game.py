"""
5 4
1 1 0
1 1 1 1
1 0 0 1
1 0 0 1
1 0 0 1
1 1 1 1
"""
map_size = list(map(int, input().split()))
start = list(map(int, input().split()))

map_data = []
for i in range(map_size[0]):
    map_data.append(list(map(int, input().split())))


dir_dict = {
    0: [(-1, 0), (0, -1), (1, 0), (0, 1)],
    1: [(0, 1), (-1, 0), (0, -1), (1, 0)],
    2: [(1, 0), (0, 1), (-1, 0), (0, -1)],
    3: [(0, -1), (1, 0), (0, 1), (-1, 0)]
}

y = start[0]
x = start[1]
direction = start[2]
count = 1

while 1:
    move = False
    for idx, dir in enumerate(dir_dict[direction]):
        n_y = y + dir[0]
        n_x = x + dir[1]

        if n_x < 0 or n_y < 0 or n_y >= map_size[0] or n_x >= map_size[1]:
            continue

        if map_data[n_y][n_x] == 0:
            map_data[y][x] = 1
            y = n_y
            x = n_x

            direction = (idx + direction) % 4
            count += 1
            move = True
            break

    t_y = y - dir_dict[direction][0][0]
    t_x = x - dir_dict[direction][0][1]

    if t_y < 0 or t_x < 0 or t_y >= map_size[0] or t_x >= map_size[1]:
        break

    elif not move and map_data[t_y][t_x] == 1:
        break

print(count)