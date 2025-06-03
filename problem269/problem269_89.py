import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    T = LI()
    A = LI()
    B = LI()

    p1 = (A[0] - B[0]) * T[0]
    p2 = p1 + (A[1] - B[1]) * T[1]
    if p1 * p2 > 0:
        print(0)
        return
    elif p2 == 0:
        print('infinity')
        return

    ans = 1
    if p2 + p1 == 0:
        print(2)
        return
    p2 = abs(p2)
    p1 = abs(p1)
    if p2 > p1:
        print(1)
        return
    if p1 % p2 == 0:
        ans -= 1
    ans += (p1 // p2) * 2
    print(ans)

if __name__ == '__main__':
    main()