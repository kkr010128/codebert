import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = float('inf')
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    _LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()
    DD = ((1,0),(0,1),(-1,0),(0,-1))

    N = NI()
    A = LI()

    # 1000までの素数列
    t = [True] * 1000
    for i in range(2,33):
        j = 2
        while i * j < 1000:
            t[i*j] = False
            j += 1
    p = []
    for i in range(2,1000):
        if t[i]: p.append(i)

    cnt = [0] * 1000000
    for x in A:
        nf = True
        for d in p:
            if d > x: break
            if x % d == 0:
                while x % d == 0:
                    x //= d
                if cnt[d]:
                    nf = False
                    break
                cnt[d] += 1
        else:
            if x > 1:
                if cnt[x]:
                    nf = False
                    break
                cnt[x] += 1
            continue
        if nf: continue
        break
    else:
        print('pairwise coprime')
        return

    g = A[0]
    for x in A[1:]:
        g = math.gcd(g,x)
        if g == 1:
            print('setwise coprime')
            return
    print('not coprime')

if __name__ == '__main__':
    main()