"""
https://programmers.co.kr/learn/courses/30/lessons/42889

5	[2, 1, 2, 6, 2, 4, 3, 3]
"""


def solution(N, stages):

    stages.sort()

    total = len(stages)
    fail_rate = {}
    for i in range(1, N+1):
        count = 0
        for stage in stages:
            if stage == i:
                count += 1
        fail_rate[i] = count / total if total != 0 else 0
        total -= count

    answer = [data[0] for data in sorted(fail_rate.items(), key=lambda x: [-x[1], x[0]])]
    return answer


result = solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
print(result)
