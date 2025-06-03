from sys import stdin
input = stdin.readline


def main():
  H, N = list(map(int, input().split()))
  A = [0]*N
  B = [0]*N
  for i in range(N):
    A[i], B[i] = map(int, input().split())

  # dp = [[0]*(H+1) for _ in range(N+1)]
  dp = [0]*(H+1)
  for j in range(H+1):
    dp[j] = float('inf')
  dp[0] = 0

  for i in range(1, N+1):
    for j in range(1, H+1):
      # dp[i][j] = dp[i-1][j]
      if j > A[i-1]:
        dp[j] = min(dp[j], dp[j-A[i-1]]+B[i-1])
      else:
        dp[j] = min(dp[j], B[i-1])

  # for i in range(N+1):
  #   print(dp[i])
  print(dp[H])


if(__name__ == '__main__'):
  main()