import math


def solution(s):
    length = len(s)
    max_split = math.floor(length / 2)

    zipped_length = length
    for d in range(1, max_split + 1):
        result = ""
        temp_str = ""
        temp_cnt = 0
        for i in range(0, length, d):
            if temp_cnt == 0:
                temp_cnt = 1
                temp_str = s[i:i + d]
                continue

            if temp_str == s[i:i + d]:
                temp_cnt += 1
            else:
                if temp_cnt > 1:
                    temp_str = str(temp_cnt) + temp_str
                result += temp_str
                temp_str = s[i:i + d]
                temp_cnt = 1

        if temp_cnt > 1:
            temp_str = str(temp_cnt) + temp_str
        result += temp_str

        if zipped_length >= len(result):
            zipped_length = len(result)
        print(result)
    return zipped_length


length = solution("aabbaccc")
print(length)