N = int(input())
S = list(input())
ans = 'No'
if N%2 == 0:
  num = int(N/2)
  pre = S[:num]
  suf = S[num:]
  if pre == suf: ans = "Yes"
print(ans)