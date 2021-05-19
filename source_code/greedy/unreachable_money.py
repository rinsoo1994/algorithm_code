# 만들 수 없는 양의 최소값 구하기
# from itertools import combinations
#
# N = int(input())
# coin_list = list(map(int, input().split()))
#
# coin_list.sort()
#
# result_list = []
# # 1 1 2 3 9
# for i in range(N):
#     combinations_list = combinations(coin_list, i+1)
#     for comb in combinations_list:
#         result_list.append(sum(comb))
#
# print(result_list)
# result_list = list(set(result_list))
# result_list.sort()
#
# for idx, data in enumerate(result_list):
#     if idx == len(result_list)-1:
#         print(data + 1)
#
#     if result_list[idx+1] - data >= 2:
#         print(data + 1)
#         break

N = int(input())
coin_list = list(map(int, input().split()))

coin_list.sort()
target = 1
for d in coin_list:
    if target < d:
        print(target)
        break

    target += d
