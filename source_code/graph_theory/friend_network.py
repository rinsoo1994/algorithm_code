from sys import stdin


def find(x):
    if parent[x] == x:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p


def union(x, y):
    x, y = find(x), find(y)
    print("befor", number)
    if x != y:
        parent[y] = x
        number[x] += number[y]
    # print(number[x])
    print("after", number)
"""
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
"""

for _ in range(int(stdin.readline())):
    num = int(stdin.readline())
    parent, number = {}, {}
    for i in range(num):
        print("parent", parent)
        print("number", number)
        a, b = stdin.readline().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)
