input_data = input()
start = [int(ord(input_data[0]))-int(ord(input_data[0]))+1, int(input_data[1])]

steps = [(1, 2), (-1, -2), (-1, 2), (1, -2), (2, 1), (-2, -1), (-2, 1), (2, - 1)]
count = 0

for step in steps:
    nx = start[0] + step[0]
    ny = start[1] + step[1]

    if nx >= 1 or ny >= 1 or nx <= 8 or ny <= 8:
        count += 1


print(count)