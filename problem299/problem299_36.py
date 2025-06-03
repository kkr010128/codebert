n = int(input())
a = list(map(int,input().split()))
d = {}
ans = ''

for i in range(0,n):
  d[a[i]] = i+1

d_sorted = sorted(d.items(), key=lambda x:x[0])

for i in range(n):
  if ans != '':
    ans = ans + ' '
  ans = ans + str(d_sorted[i][1])

print(ans)