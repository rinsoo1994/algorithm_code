
from collections import deque


def solution(n, computers):
    computer_dict = {}
    for idx1, computer in enumerate(computers):
        idx_1 = idx1+1
        if not idx_1 in computer_dict:
            computer_dict[idx_1] = []

        for idx2, network in enumerate(computer):
            idx_2 = idx2 + 1
            if idx_2 > idx_1 and network:
                computer_dict[idx_1].append(idx_2)

    q = deque()
    visited = []
    count = 0
    for i in range(1, n+1):
        if i not in visited:
            visited.append(i)
            q.append((i, count+1))

        while q:
            no, count = q.popleft()
            for nw in computer_dict[no]:
                if nw not in visited:
                    q.append((nw, count))
                    visited.append(nw)

    return count


computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
count = solution(3, computers)
print(count)
#
# n = 3
#
# 1 2
# 2 3, 4
# 4
#
#
#
# # 돌면서
# for i in range(n):
#