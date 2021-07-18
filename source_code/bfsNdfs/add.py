numbers = [1, 1, 1, 1, 1]
target = 3
answer = 0


def dfs(idx, numbers, target, value, typ):
    global answer
    N = len(numbers)

    print(idx, value, answer, typ)
    if idx == N and target == value:
        answer += 1
        print("return")
        return

    if idx == N:
        print("return")
        return

    dfs(idx+1, numbers, target, value+numbers[idx], "plus")
    dfs(idx+1, numbers, target, value-numbers[idx], "minus")


def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0, None)
    return answer


answer = solution(numbers, target)
print(answer)
