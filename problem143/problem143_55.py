K = int(input())
S = input()

if len(S) <= K:
  ans = S
else:
  ans = S[0:K] + '...'

print(ans)