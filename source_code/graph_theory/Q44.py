"""
Q.44 행성터널

5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""
import copy


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def get_min_num(dim1, dim2):
    return min(abs(dim1[0]-dim2[0]), abs(dim1[1]-dim2[1]), abs(dim1[2]-dim2[2]))


N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [i for i in range(N + 1)]

for num in range(1, N+1):
    x, y, z = map(int, input().split())
    graph[num] = [x, y, z]


min_cycle = 10e9


def main():
    for num in range(1, N+1):
        for cycle_num in range(num, N+1):
            make_cycle(num, cycle_num)