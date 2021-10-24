
def divide_balanced_str(p_string):
    count_dict = {"(": 0, ")": 0}

    for idx, s in enumerate(p_string):
        count_dict[s] += 1
        if count_dict["("] == count_dict[")"]:
            return p_string[:idx+1], p_string[idx+1:]

    return p_string, ""


def check_right_str(p_string):
    temp = ""
    count_dict = {"(": 0, ")": 0}

    for idx, s in enumerate(p_string):
        if not temp:
            temp = s
        count_dict[s] += 1
        if count_dict[")"] > count_dict["("]:
            return False

    return True


def solution(p):
    if not p:
        return ""

    u, v = divide_balanced_str(p)
    if check_right_str(u):
        answer = u + solution(v)
    else:
        tmp = ""
        for d in u[1:-1]:
            if d == "(":
                tmp += ")"
            else:
                tmp += "("
        answer = "(" + solution(v) + ")" + tmp

    return answer


result = solution("(()())()")
print(result)
result = solution(")(")
print(result)
result = solution("()))((()")
print(result)
result = solution(")()(")
print(result)
