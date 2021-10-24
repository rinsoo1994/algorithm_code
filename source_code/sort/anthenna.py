import math
N = int(input())
houses = list(map(int, input().split(" ")))

sorted_houses = sorted(houses)

mid_idx = math.floor((len(sorted_houses)-1)/2)
print(sorted_houses[mid_idx])
