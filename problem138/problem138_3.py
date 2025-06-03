import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    N,S=map(int,input().split())
    A=list(map(int,input().split()))

    # https://qiita.com/drken/items/dc53c683d6de8aeacf5a#%E9%A1%9E%E9%A1%8C-3
    
    INF = 10**10  # INF+INFを計算してもオーバーフローしない範囲で大きく
    MOD=998244353
    
    I, J =N,S
    # dpテーブル dp[i][j]:=i番目以下で選ばれしa_kの和がjになる通り数
    dp = [[0]*(J+1) for _ in range(I+1)]
    # 初期条件
    dp[0][0] = 1
    # ループ
    for i in range(I):
        for j in range(J+1):
            dp[i+1][j]+=2*dp[i][j]
            dp[i+1][j]%=MOD
            if j+A[i]<=S:
                dp[i+1][j+A[i]]+=dp[i][j]
                dp[i+1][j+A[i]]%=MOD

    print(dp[I][J])
    
    
    
resolve()