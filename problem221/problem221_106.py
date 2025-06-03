S = list(input())

# 問題文の通りに実装する
n = len(S)
for i in range(n):
  S[i] = 'x'

ans = ''
for i in range(n):
  ans += S[i]

print(ans)