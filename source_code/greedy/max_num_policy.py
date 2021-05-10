"""
    greedy algorithm

    탐욕알고리즘은 기본적으로 최적의 해를 구하지 않아도 될떄를 고려하여 사용하여야한다.
    즉 같은 문제더라도 값에 따라 탐욕법을 쓸 수 있는때와 아닌 때가 따로 있다는 것이다.
"""


def simple_max_num_policy(input_list, K, M):
    """
    :param input_list: input list data
    :param K:
    :param M:
    :return: result list data
    """
    max_num = input_list[-1]
    second_num = input_list[-2]

    div, mod = divmod(M, (K + 1))
    sum_result = (K * max_num + second_num) * div + mod * max_num
    return sum_result


def max_num_policy(input_list, K, M):
    """
    :param input_list: input list data
    :param K:
    :param M:
    :return: result list data
    """
    continue_flag = True
    max_num_flag = 1

    input_data.sort()
    max_num_list = []

    max_num = input_list[-1]
    second_num = input_list[-2]

    while continue_flag:
        for i in range(K):
            if len(max_num_list) == M:
                continue_flag = False
                break
            if max_num_flag == 1:
                max_num_list.append(max_num)
            else:
                if i == 0:
                    max_num_list.append(second_num)
                else:
                    continue

        max_num_flag = 0 if max_num_flag == 1 else 1

    return sum(max_num_list)


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    input_data = list(map(int, input().split()))

    result1 = max_num_policy(input_data, k, m)
    result2 = simple_max_num_policy(input_data, k, m)

    print(result1)
    print(result2)
