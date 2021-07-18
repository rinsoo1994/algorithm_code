
from collections import deque


def dfs(num, computers, visited, n):
    visited[num] = True
    for i in range(n):
        if computers[num][i] == 1 and visited[i] == 0:
            visited[i] = True
            dfs(i, computers, visited, n)


def bfs(num, computers, visited, n):
    q = deque()
    q.append(num)
    visited[num] = True

    while q:
        no = q.popleft()
        for i in range(n):
            if computers[no][i] == 1 and visited[i] == 0:
                visited[i] = True
                q.append(i)


def solution(n, computers):

    visited = [False for _ in range(n)]
    count = 0

    for i in range(0, n):
        if not visited[i]:
            dfs(i, computers, visited, n)
            count += 1

    # print(visited)
    return count


computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
count = solution(3, computers)
print(count)
