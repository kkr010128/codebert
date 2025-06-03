n,m = map(int, input().split())
l = list(map(int, input().split()))
c = 0
for index in l:
  if index >= sum(l)/(4*m):
    c += 1
print("Yes" if c >= m else "No")