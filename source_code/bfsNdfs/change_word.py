answer = 10e9


def dfs(begin, target, words, count, visited):
    global answer
    if begin == target:
        answer = min(answer, count)
        return

    for word in words:
        if word in visited:
            continue

        diff_count = 0
        for i in range(len(word)):
            if word[i] != begin[i]:
                diff_count += 1
        if diff_count == 1:
            visited.append(word)
            dfs(word, target, words, count + 1, visited)
            visited.pop(-1)


def solution(begin, target, words):
    global answer
    count = 0
    visited = [begin]
    dfs(begin, target, words, count, visited)

    if answer == 10e9:
        answer = 0

    return answer


result = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	)


if answer == 10e9:
    answer = 0
print(result)