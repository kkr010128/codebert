#coding:utf-8
import sys
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = lambda *something : print(*something) if DEBUG else 0
DEBUG = False
def main(given = sys.stdin.readline):
    from math import floor
    input = lambda : given().rstrip()
    LMIIS = lambda : list(map(int,input().split()))
    II = lambda : int(input())
    XLMIIS = lambda x : [LMIIS() for _ in range(x)]

    N,K = LMIIS()
    A = LMIIS()
    F = LMIIS()


    F.sort()    
    A.sort(reverse=True)


    def f(x):
        sum_diff = 0
        for a,f in zip(A,F):
            if a*f-x > 0:
                sum_diff += a-x//f
        return True if sum_diff <= K else False
    l = -1
    r = 10**13
    while r-l>1:

        m = (l+r)//2
        if f(m):
            r = m
        else:
            l = m
    print(r)











if __name__ == '__main__':
    main()