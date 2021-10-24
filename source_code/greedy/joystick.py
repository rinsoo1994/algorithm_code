def solution(name):

    min_num, max_num = ord("A"), ord("Z")
    ord_name = [ord(n) for n in name]
    result = [min(abs(n - min_num), abs(n - max_num) + 1) for n in ord_name]

    count = 0
    for a in name[::-1]:
        if a == "A":
            count += 1
        else:
            break

    count_b = 0
    for b in name[1:]:
        if b == "A":
            count_b += 1
        else:
            break

    count_c = 0
    for a in name[1:]:
        if a != "A":
            count_c += 1
        else:
            break
    count_d = 0
    for b in name[count_c-1:]:
        if b == "A":
            count_b += 1
        else:
            break

    right_side = len(name) - 1 - count
    left_side = len(name) - 1 - count_b
    left_and_right = count_c * 2 + count_d
    direction = min(right_side, left_side, left_and_right)

    return sum(result) + direction


result = solution("ABAAAAAAAAABB")
print(result)