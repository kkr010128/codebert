def solve():
  N, K, C = map(int, input().split())
  S = input()
  l_r,r_l = [0]*N,[0]*N
  i,cnt = 0,0
  while i<N and cnt<K:
    if S[i]=='o':
      l_r[i] = 1
      cnt += 1
      i += C
    i += 1
  j,cnt = N-1,0
  while j>=0 and cnt<K:
    if S[j]=='o':
      r_l[j] = 1
      cnt += 1
      j -= C
    j -= 1
  ans = []
  c_lr = 0
  c_rl = 0
  for i in range(1,N+1):
    if l_r[i-1]:
      c_lr += 1
    if r_l[i-1]:
      c_rl += 1
    if l_r[i-1]*r_l[i-1]==1 and c_lr==c_rl:
      ans.append(i)
  return ans
print(*solve(),sep='\n')