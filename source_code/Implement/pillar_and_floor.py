

def check_build(result):
    for build in result:
        if build[2] == 1:
            if [build[0], build[1]-1, 0] in result or [build[0] +1, build[1]-1, 0] in result or ([build[0] -1, build[1], 1] in result and [build[0] +1, build[1], 1] in result):
                continue
            return False
        # 0은 기둥
        elif build[2] == 0:
            if build[1] == 0 or [build[0] - 1, build[1], 1] in result or [build[0], build[1]-1, 0] in result or [build[0], build[1], 1] in result:
                continue
            return False
    return True


def solution(n, build_frame):
    result = []

    for build in build_frame:
        if build[3] == 1:
            result.append(build[:3])
            if not check_build(result):
                result.remove(build[:3])

        if build[3] == 0:
            result.remove(build[:3])

            ch = check_build(result)
            if not ch:
                result.append(build[:3])

    result.sort(key=lambda x: (x[0], x[1]))
    return result


# result = solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
result = solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
print(result)