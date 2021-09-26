"""
    Q9. 문자열 압축

"""


def compression(words, comp_len):
    compression_word = ""

    temp_word = ""
    temp_count = 0

    for num in range(0, len(words), comp_len):
        if not temp_word:
            temp_word = words[num:num + comp_len]
            temp_count += 1
        else:
            if temp_word == words[num:num + comp_len]:
                temp_count += 1
            else:
                compression_word += str(temp_count) + temp_word
                temp_count = 1
                temp_word = words[num:num + comp_len]

    compression_word += str(temp_count) + temp_word
    compression_word = compression_word.replace("1", "")
    return len(compression_word)


def solution(s):
    length = len(s)
    mid_length = int(length/2)

    compression_num = len(s)
    for num in range(1, mid_length+1):
        compression_num = min(compression_num, compression(s, num))

    return compression_num


result = solution("aabbaccc")
print("result", result)
result = solution("ababcdcdababcdcd")
print("result", result )

result = solution("abcabcdede")
print("result", result )

result = solution("abcabcabcabcdededededede")
print("result", result )

result = solution("xababcdcdababcdcd")
print("result", result )
