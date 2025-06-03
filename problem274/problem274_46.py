def solve():
  N, M = map(int, input().split())
  S = input()
  ans = []
  visited = [False]*(N+1)
  visited[-1] = True
  now = N
  while True:
    i = min(M,now)
    visited[now-i] = True
    while S[now-i]=='1':
      i -= 1
      if visited[now-i]==True:
        return [-1]
      visited[now-i] = True
    ans.append(i)
    if now-i==0:
      return ans[::-1]
    now -= i
print(*solve())