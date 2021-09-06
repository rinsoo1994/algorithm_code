"""
Q.42 탑승구

INPUT1
4
3
4
1
1

INPUT2
4
6
2
2
3
3
4
4
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    else:
        parent[x] -= 1
    return parent[x]


G = int(input())
P = int(input())

parent = [num for num in range(G+1)]

count = 0
for i in range(P):
    doking = int(input())
    parent_num = find_parent(parent, doking)

    if parent_num == -1:
        break
    else:
        count += 1

