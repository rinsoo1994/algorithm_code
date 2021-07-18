import itertools
import copy


def solutions(n, weak, dist):
    dst = copy.deepcopy(dist)
    dst.sort(reverse = True)
    for i in range(1, len(dst)+1):
        for item in itertools.combinations(range(len(weak), i)):
            d = []
            for j in range(i):
                d.append((weak[item[(j+1)%i]-1]-weak[item[j]]+n)%n)
            d.sort(reverse=True)
            rst=True
            for j in range(i):
                if dst[j]<d[j]:
                    rst=False
                    break
            if rst:
                return i
        return -1