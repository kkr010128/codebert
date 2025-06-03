def solve():
  ans = -float('inf')
  N, K = map(int, input().split())
  P = list(map(lambda x:int(x)-1, input().split()))
  C = list(map(int, input().split()))
  for i in range(N):
    score = 0
    now = i
    visited = [-1]*N
    scores = [0]*N
    visited[now] = 0
    for j in range(1,K+1):
      now = P[now]
      score += C[now]
      ans = max(ans, score)
      if visited[now]>=0:
        cyc = j - visited[now]
        up = score - scores[now]
        break
      scores[now] = score
      visited[now] = j
    else:
      continue
    if up<=0:
      continue
    cnt = j+1
    if K-cyc>=j:
      score += (K-cyc-j)//cyc * up
      ans = max(ans, score)
      cnt += (K-cyc-j)//cyc*cyc
    for j in range(cnt,K+1):
      now = P[now]
      score += C[now]
      ans = max(ans, score)
  return ans
print(solve())