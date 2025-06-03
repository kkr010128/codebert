
def solve():
    dp = [0] * N
    for i in range(N):
        dp[A[i]-1] = i+1
    for i in range(N):
        print(dp[i], end=" ")


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    solve()  
