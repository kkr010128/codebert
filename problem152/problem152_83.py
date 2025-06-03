import sys
sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))
def resolve():
    N = ir()
    pos = []
    neg = []
    tot = 0
    for i in range(N):
        tmp = 0
        b = 0
        for c in sr():
            if c == '(':
                tmp += 1
            else:
                tmp -= 1
                b = min(b, tmp)
        if tmp > 0:
            pos.append([tmp, b])
        else:
            neg.append([-tmp, b-tmp])
        tot += tmp
    if tot != 0:
        print('No')
        return
    pos = sorted(pos, key=lambda x: (x[1], x[0]))[::-1]
    neg = sorted(neg, key=lambda x: (x[1], x[0]))[::-1]
    c = 0
    for p in pos:
        t, b = p
        if c+b < 0:
            print('No')
            return
        c += t
    c = 0
    for n in neg:
        t, b = n
        if c+b < 0:
            print('No')
            return
        c += t
    print('Yes')
    return
resolve()