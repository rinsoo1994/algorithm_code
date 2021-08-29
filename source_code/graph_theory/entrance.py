"""
Q.42 탑승구

4
3
4
1
1
"""


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


# 탑승구 개수
g = int(input())
# 비행기 개수
p = int(input())

parent = [0] * (g+1)

for i in range(1, g+1):
    parent[i] = i

parent = [0, 1, 2, 3, 4]


result = 0
for _ in range(p):
    # 현재 비행기의 탑승구의 루트 확인
    # [0, 0, 2, 3, 3]
    data = find_parent(parent, int(input()))
    # 현재 루트가 0이면 종료
    if data == 0:
        break

    # 현재 루트가 0이 아니면 왼쪽 집합과 합치기
    # find_parent([0, 1, 2, 3, 4], 4)
    union_parent(parent, data, data - 1)
    result += 1

print(result)