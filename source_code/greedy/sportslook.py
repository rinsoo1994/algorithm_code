def solution(n, lost, reserve):

    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]

    result = [0 for i in range(n + 1)]

    for res in range(n):
        if (res + 1) not in _lost:
            result[res + 1] = 1

    for r in _reserve:
        f = r - 1
        b = r + 1
        print(f, b)
        if f in _lost:
            print("zzz")
            _lost.remove(f)
        elif b in _lost:
            print("ggg")
            _lost.remove(b)

    return result.count(1)

solution(5, [2, 4],	[1, 3, 5]	)
