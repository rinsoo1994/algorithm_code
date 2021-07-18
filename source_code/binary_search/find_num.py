"""
Q.27 정렬된 배열에서 특정 수의 개수 구하기

7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
"""

n, x = map(int, input().split())
data = list(map(int, input().split()))


result = data.count(x)
if result == 0:
    result = -1

print(result)

