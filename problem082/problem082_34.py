s = input()
t = input()

ans = []

for i in range(0, len(s) - len(t) + 1):
  score = 0
  # sをtと同じ文字列分、切り取る
  u = s[i:i + len(t)]
  for j in range(len(t)):
    # 切り取った文字列のsとtが同じかどうか比較する
    if u[j] != t[j]:
      score += 1
  ans.append(score)

print(min(ans))
