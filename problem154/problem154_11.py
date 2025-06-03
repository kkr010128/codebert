n,k = [int(x) for x in input().split()]
d = []
a = []
for i in range(k):
  d.append(int(input()))
  a.append([int(x) for x in input().split()])
#print(a)
ans = [0] * (n + 1)
for i in range(k):
  for j in range(d[i]):
    #print(a[i][j])
    ans[a[i][j]] += 1
c = 0
for i in range(1,n + 1):
  if ans[i] == 0:
    c += 1
print(c)