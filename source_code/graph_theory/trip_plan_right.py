"""
Q 41. 여행 계획

5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 5 3

"""


def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    print("find_parent", parent, x)
    if parent[x] != x:
        print("parent[x] != x", parent[x], x)
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [0] * (N + 1)

for i in range(1, N+1):
    parent[i] = i


for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

print(parent)
trip_plan = list(map(int, input().split()))

result = True
for i in range(M-1):
    if find_parent(parent, trip_plan[i]) != find_parent(parent, trip_plan[i+1]):
        result = False

print(result)