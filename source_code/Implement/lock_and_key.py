

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False

    return True


def rotate_90_degree(key):

    n = len(key)
    m = len(key[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j]
    return result


def solution(key, lock):
    # triple_list = [[0] * len(key) * 3] * )
    n = len(lock)
    m = len(key)
    triple_list = [[0] * len(lock) * 3 for d in range(len(lock[0] * 3))]
    # 배열 크기 세배 키움

    for idx1, data1 in enumerate(lock):
        for idx2, data2 in enumerate(data1):
            triple_list[idx1+len(lock)][idx2+len(lock[0])] = data2

    result = False
    for i in range(4):
        key = rotate_90_degree(key)
        for x in range(n * 2):
            for y in range(n * 2):

                for i in range(m):
                    for j in range(m):
                        triple_list[i + x][y + j] += key[i][j]

                if check(triple_list) == True:
                    return True
                else:
                    for i in range(m):
                        for j in range(m):
                            triple_list[i + x][y + j] -= key[i][j]

    return False


if __name__ == '__main__':
    result = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
    print(result)