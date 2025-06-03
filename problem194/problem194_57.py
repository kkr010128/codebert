def resolve():
  H, W = map(int, input().split(" "))
  s = []
  dp = [[0] * W for i in range(H)]
  for _ in range(H):
    s.append([x == "." for x in list(input())])

  for h in range(H):
    for w in range(W):
      if h == 0 and w == 0:
        if not s[0][0]:
          dp[0][0] = 1

      elif h == 0:
        dp[0][w] = dp[0][w-1]
        if s[0][w-1] and not s[0][w]:
          dp[0][w] += 1

      elif w == 0:
        dp[h][0] = dp[h-1][0]
        if s[h-1][0] and not s[h][0]:
          dp[h][0] += 1

      else:
        # 左側と上側を見て、操作回数が最小になるようにする。
        # 上だけをみる
        temp_up = dp[h-1][w]
        if s[h-1][w] and not s[h][w]:
          temp_up += 1

        # 左だけを見る
        temp_left = dp[h][w-1]
        if s[h][w-1] and not s[h][w]:
          temp_left += 1

        dp[h][w] = min(temp_up, temp_left)

  print(dp[H-1][W-1])

if __name__ == "__main__":
  resolve()