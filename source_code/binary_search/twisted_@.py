big = 0
small = 0




N = int(input())
data = list(map(int,  input().split()))


for idx, d in enumerate(data):
    if d > idx:
        big += 1
    else:
        small+1