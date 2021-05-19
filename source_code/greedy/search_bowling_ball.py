N, M = map(int, input().split())
weight_list = list(map(int, input().split()))

array = [0] * 11
for x in weight_list:
    array[x] += 1

result = 0
for i in range(1, M + 1):
    N -= array[i]
    result += array[i] * N

print(result)