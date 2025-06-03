#coding:utf-8
import sys
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = lambda *something : print(*something) if DEBUG else 0
DEBUG = True
def main(given = sys.stdin.readline):
    input = lambda : given().rstrip()
    LMIIS = lambda : list(map(int,input().split()))
    II = lambda : int(input())
    XLMIIS = lambda x : [LMIIS() for _ in range(x)]

    N,T = LMIIS()
    AB = []
    for i in range(N):
        AB.append(LMIIS())
    
    AB.sort()
    dp = [-1] * (T+3000)
    dp[0] = 0
    for a,b in AB:
        tmpdp = dp[:]
        for j in range(T):
            if dp[j] != -1:
                tmpdp[j+a] = max(dp[j+a],dp[j]+b)
        dp = tmpdp
    print(max(dp))






if __name__ == '__main__':
    main()