#!python3

import sys

iim = lambda: map(int, input().rstrip().split())

def popcnt2(n):
    a = (
        0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8,
    )
    ans = 0
    while n:
        ans += a[n&0xff]
        n >>= 8
    return ans

def resolve():
    N = int(input())
    S = list(input())
    Q = int(input())

    ln = N.bit_length() + 1
    c0 = ord('a')
    smap = [1<<(i-c0) for i in range(c0, ord('z')+1)]

    T = [None] * ln

    T[0] = [smap[ord(S[i])-c0] for i in range(N)]
    if N&1:
        T[0].append(0)
        N += 1

    t0, n2 = T[0], N
    for i in range(1, ln):
        n1 = n2 = n2 >> 1
        if n2 & 1:
            n2 += 1
        ti = T[i] = [0] * n2
        for j in range(n1):
            j2 = j << 1
            d1, d2 = t0[j2], t0[j2+1]
            ti[j] = d1 | d2
        t0 = ti

    #for ti in T:
    #    print(len(ti), ti)
    ans = []
    for cmd, i, j in (line.split() for line in sys.stdin):
        i = int(i) - 1
        if cmd == "1":
            if S[i] == j:
                continue

            S[i] = j

            t0 = T[0]
            t0[i] = smap[ord(j)-c0]
            for i1 in range(1, ln):
                ti = T[i1]
                j1 = i >> 1
                ti[j1] = t0[i] | t0[i^1]
                i, t0 = j1, ti
            #for ti in T:
            #    print(len(ti), ti)
        elif cmd == "2":
            j = int(j) - 1

            d1 = 0
            for i1 in range(ln):
                ti = T[i1]
                if not i < j :
                    if i == j:
                        d1 |= ti[i]
                    break
                if i & 1:
                    d1 |= ti[i]
                    i += 1
                if j & 1 == 0:
                    d1 |= ti[j]
                    j -= 1

                i >>= 1; j >>=1

            ans.append(popcnt2(d1))

    print(*ans, sep="\n")

if __name__ == "__main__":
    resolve()
