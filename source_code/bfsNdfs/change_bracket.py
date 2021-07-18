from collections import deque
def check_right(p):
    q = []
    for bracket in p:
        if q:
            if bracket == ")":
                last = q.pop(-1)
                if last != "(":
                    return False
            else:
                q.append(bracket)
        else:
            if bracket == ")":
                return False
            q.append(bracket)

    return True


def check_balanced(p):
    bracket_count = {}
    u, v = "", ""
    for idx, bracket in enumerate(p):
        if bracket not in bracket_count:
            bracket_count[bracket] = 0
        bracket_count[bracket] += 1

        if idx != 0 and bracket_count.get("(", 0) == bracket_count.get(")", 0):
            u, v = p[:idx+1], p[idx+1:]
            break

    return u, v


def reverse_string(p):
    result = ""
    for bracket in p:
        if bracket == "(":
            result += ")"
        else:
            result += "("

    return result


def change_bracket(p):
    if not p:
        return p

    u, v = check_balanced(p)
    if check_right(u):
        cr_result = u + change_bracket(v)
    else:
        cr_result = "(" + change_bracket(v) + ")" + reverse_string(u[1:-1])

    return cr_result


def solution(p):
    answer = change_bracket(p)

    return answer
