import itertools
from typing import List


def main():
    h, w, k = map(int, input().split())
    c = []
    for _ in range(h):
        c.append(list(input()))

    print(hv(c, h, w, k))


def hv(c: List[List[str]], h: int, w: int, k: int) -> int:
    ret = 0
    for comb_h in itertools.product((False, True), repeat=h):
        for comb_w in itertools.product((False, True), repeat=w):
            cnt = 0
            for i in range(h):
                for j in range(w):
                    if comb_h[i] and comb_w[j] and c[i][j] == '#':
                        cnt += 1
            if cnt == k:
                ret += 1
    return ret


if __name__ == '__main__':
    main()
