n = int(input())
A = list(map(int, input().split(' ')))
q = int(input())
M = list(map(int, input().split(' ')))

dp = {}

# Aの要素のうちp番目以降を組み合わせてtを作れるか?
def solve(p, t):
  if ((p, t) in dp):
    return dp[(p, t)]

  if (p == n):
    # 使う/使わないの枝をたどって0になったらOK
    return t == 0

  # p番目を使ったらtを引いて次へ, 使わなければtのまま次へ
  ans = solve(p+1, t-A[p]) or solve(p+1, t)
  dp[(p, t)] = ans
  return ans

for m in M:
  print("yes" if solve(0, m) else "no")

