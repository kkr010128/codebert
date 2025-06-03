def main():
  import sys
  input = sys.stdin.readline

  r,c,k = map(int,input().split())
  b = [[0 for _ in range(c)] for _ in range(r)]
  for i in range(k):
    y,x,v = map(int,input().split())
    y -= 1
    x -= 1
    b[y][x] = v

  # dp[j][l]:(i,j)に居て、i行目のアイテムをl個拾ったときの価値最大値。
  dp = [[0 for _ in range(4)] for _ in range(c+1)]
  for i in range(r):
    for j in range(c):
      # アイテムを拾う遷移。個数が多い方から計算する。
      for l in range(2,-1,-1):
        dp[j][l+1] = max(dp[j][l]+b[i][j],dp[j][l+1])
      # 移動する遷移。行を移動する際は、拾ったアイテム数はリセットされる。
      for l in range(4):
        dp[j+1][l] = max(dp[j][l],dp[j+1][l])
        dp[j][0] = max(dp[j][l],dp[j][0])
  ans = 0
  for i in range(4):
    ans = max(dp[c-1][i],ans)
  print(ans)

main()