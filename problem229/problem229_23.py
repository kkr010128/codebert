import sys
input = sys.stdin.readline
def main():
    H, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A_max = max(A)
    dp = [1e14] * (H+A_max + 1) # ダメージ量がiの最小コスト
    dp[0] = 0
    for i in range(H):
        for j in range(N):
            dp[i+A[j]] = min(dp[i+A[j]], dp[i]+B[j])

    ans = 1e30
    for i in range(H, H+A_max+1):
        ans = min(ans, dp[i])
    print(ans)
main()