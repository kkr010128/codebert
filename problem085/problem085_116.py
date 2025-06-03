import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from collections import defaultdict
def main():
    n, *a = map(int, read().split())

    maxa = max(a) + 1  # aはint配列
    d = [i for i in range(maxa)]
    for p0 in range(2, maxa):
        if p0 == d[p0]:
            for p1 in range(p0 ** 2, maxa, p0):
                if d[p1] % p0 == 0:
                    d[p1] = p0

    def factorization(f):  # f > maxaだとエラー
        l = []
        t = f
        while True:
            if t == d[t]:
                l.append(d[t])
                break
            else:
                l.append(d[t])
                t = t // d[t]
        return l

    if all([i == 1 for i in a]):
        print('pairwise coprime')
        sys.exit()
    if len(set(a)) == 1:
        print('not coprime')
        sys.exit()
    d1 = defaultdict(int)
    for ae in a:
        t1 = set(factorization(ae))
        for t1e in t1:
            d1[t1e] += 1
    if 1 in a:
        d1[1] = 1
    d1v = tuple(d1.values())
    if all([i == 1 for i in d1v]):
        print('pairwise coprime')
    elif max(d1v) == n:
        print('not coprime')
    else:
        print('setwise coprime')

if __name__ == '__main__':
    main()