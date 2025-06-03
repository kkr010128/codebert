def main():
  n = int(input())
  MOD = int(1e9 + 7)
  dp = [0 for _ in range(n + 1)]
  dp[0] = 1
  for i in range(3 , n+1):
    dp[i] = 1
    for j in range(3,i - 2):
      if i - j < 3:
        break
      dp[i] = (dp[i] + dp[i - j])%MOD
  print(dp[n])
  

if __name__ == "__main__":
  main()