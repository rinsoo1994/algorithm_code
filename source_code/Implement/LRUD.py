N = int(input())
data = list(map(str, input().split()))

direction = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
current_location = [1, 1]

for d in data:
    if (current_location[0] <= 1 or current_location[1] <= 1) and (d == "L" or d == "U"):
        continue
    elif (current_location[0] > N or current_location[1] > N) and (d == "R" or d == "D"):
        continue

    current_location[0] += direction[d][0]
    current_location[1] += direction[d][1]


print(current_location)