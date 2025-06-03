import sys
sys.setrecursionlimit(10**9)

INF = 10**20
def main():
    H,N = map(int,input().split())
    A,B = [],[]
    for _ in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)

    tp = 3 * 10**4
    dp = [INF] * tp
    dp[0] = 0
    ans = INF
    for h in range(tp):
        minim = INF
        for i in range(N):
            dp_i = h-A[i]
            if dp_i >= 0 and dp[dp_i] != INF:
                minim = min(minim,dp[dp_i]+B[i])
                # print(dp[h-A[i]]+B[i])

        if minim != INF:
            dp[h] = minim
            if h >= H:
                ans = min(ans,dp[h])


    print(ans)


if __name__ == "__main__":
  main()
