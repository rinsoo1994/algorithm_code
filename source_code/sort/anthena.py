"""
https://www.acmicpc.net/problem/18310

4
5 1 7 9
"""

n = int(input())

data = list(map(int, input().split()))
data.sort()
print(data[(n-1)//2])
