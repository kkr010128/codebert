 #12716015

n, m = map(int, input().split())
h = list(map(int, input().split()))
ans = [1]*n
for i in range(m):
  a, b= map(int, input().split())
  a -= 1
  b -= 1
  if h[a] > h[b]:
    ans[b] = 0
  elif h[a] < h[b]:
    ans[a] = 0
  if h[a] == h[b]:
    ans[a] = 0
    ans[b] = 0
print(ans.count(1))