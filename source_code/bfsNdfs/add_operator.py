"""
2
5 6
0 0 1 0

6
1 2 3 4 5 6
2 1 1 1
"""

max_num = -1000000000
min_num = 10000000000

n = int(input())
num = list(map(int, input().split()))
count = list(map(int, input().split()))


def solution(count_dict, data, sum, idx):
    global min_num, max_num
    if idx == n:

        min_num = min(sum, min_num)
        max_num = max(sum, max_num)
        return

    if count_dict["+"] > 0:
        count_dict["+"] -= 1
        solution(count_dict, num, sum+data[idx], idx + 1)
        count_dict["+"] += 1

    if count_dict["-"] > 0:
        count_dict["-"] -= 1
        solution(count_dict, num, sum-data[idx], idx + 1)
        count_dict["-"] += 1

    if count_dict["*"] > 0:
        count_dict["*"] -= 1
        solution(count_dict, num, sum*data[idx], idx + 1)
        count_dict["*"] += 1

    if count_dict["%"] > 0:
        count_dict["%"] -= 1
        if sum < 0:
            solution(count_dict, num, int(int(abs(sum) / data[idx]) * -1), idx + 1)
        else:
            solution(count_dict, num, int(sum / data[idx]), idx + 1)
        count_dict["%"] += 1


count_dict = {}
operator_list = ["+", "-", "*", "%"]

for i in range(4):
    count_dict[operator_list[i]] = count[i]

solution(count_dict, num, num[0], 1)

print(max_num)
print(min_num)

