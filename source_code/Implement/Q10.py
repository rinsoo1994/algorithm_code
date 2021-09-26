"""
Q10. 자물쇠와 열쇠
"""


def check_is_correct_key(big_lock, lock_length):
    for i in range(0, lock_length):
        for j in range(0, lock_length):
            b_i, b_j = i+lock_length, j + lock_length
            if big_lock[b_i][b_j] != 1:
                return False
    return True


def get_lotation_key(key, direction_num):
    # 키 회전하는 로직 구현
    return key


def solution(key, lock):
    big_len = len(lock) * 3
    big_lock = [[0] * big_len for _ in range(big_len)]
    lock_length = len(lock)
    key_length = len(key)
    for i in range(0, lock_length):
        for j in range(0, lock_length):
            b_i, b_j = i+lock_length, j + lock_length
            big_lock[b_i][b_j] = lock[i][j]

    # 키 사방향 회전, 좌우 이동 하면서 췍!
    for num in range(4):
        dir_key = get_lotation_key(key, num)

        for x in range(big_len):
            for y in range(big_len):

                for i in range(key_length):
                    for j in range(key_length):
                        pass

    return


result = solution([[0,0,0], [1,0,0], [0,1,1]],
                  [[1,1,1], [1,1,0],[1,0,1]])
