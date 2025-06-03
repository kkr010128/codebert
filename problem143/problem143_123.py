K = int(input())
S = input()

l = list(S)
if len(l) <= K: print(S)
else: 
  ans = ''
  for i in range(K):
    ans += l[i]
  ans += '...'
  print(ans)