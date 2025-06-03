import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N,D,A = LI()
    X = []; XH = []
    for _ in range(N):
        x,h = LI()
        X.append(x); XH.append((x,h))
    XH.sort()
    X.sort()
    down = [0] * (N+1)


    p = 0
    ans = 0
    for i in range(N):
        if p < XH[i][1]:
            b = -(-(XH[i][1]-p)//A)
            ans += b
            p += b * A
            down[bisect.bisect(X,X[i]+2*D)-1] += b*A
        p -= down[i]
    print(ans)

if __name__ == '__main__':
    main()