from collections import Counter
def solve():
  N = int(input())
  S = list(input())
  c = Counter(S)
  ans = c['R']*c['G']*c['B']
  for i in range(N):
    for j in range(i+1,N):
      k = j*2-i
      if k>N-1:
        break
      if S[i]!=S[j] and S[j]!=S[k] and S[i]!=S[k]:
        ans -= 1
  return ans
print(solve())
