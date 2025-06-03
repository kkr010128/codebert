n,m = map(int, input().split())
height = list(map(int, input().split()))
c = 0
net = [[] for i in range(n)]
for j in range(m):
  a,b = map(int, input().split())
  net[a-1].append(height[b-1])
  net[b-1].append(height[a-1])
for i in range(n):
  net[i].append(0)
  if max(net[i]) < height[i]:
    c += 1
print(c)