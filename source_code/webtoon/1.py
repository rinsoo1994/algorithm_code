import math


def solution(lottery):

    winner = 0  # 당첨된 사람 수
    lottery_dict = {}
    for lottery_data in lottery:
        if lottery_data[0] not in lottery_dict:
            lottery_dict[lottery_data[0]] = {"w": 0, "c": 0}

        if not lottery_dict[lottery_data[0]]["w"]:
            if lottery_data[1]:
                winner += 1
                lottery_dict[lottery_data[0]]["w"] = 1
                lottery_dict[lottery_data[0]]["c"] += 1
            else:
                lottery_dict[lottery_data[0]]["c"] += 1

    if not winner:
        return 0

    answer = math.floor(sum([v["c"] for k, v in lottery_dict.items() if v["w"]]) / winner)
    return answer

solution([[1,0],[2,0],[3,0]])