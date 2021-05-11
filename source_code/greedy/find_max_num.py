"""
    greedy algorithm

    탐욕알고리즘은 기본적으로 최적의 해를 구하지 않아도 될떄를 고려하여 사용하여야한다.
    즉 같은 문제더라도 값에 따라 탐욕법을 쓸 수 있는때와 아닌 때가 따로 있다는 것이다.
"""

n, m = map(int, input().split())

array_list = []
for i in range(n):
    array_list.append(list(map(int, input().split())))


max_list = []
for list_data in array_list:
    max_list.append(min(list_data))

print(max(max_list))


