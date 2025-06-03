import collections

n = int(input())
a = list(map(int, input().split()))

l = []
r = []
for i in range(n):
  l.append(i+a[i])
  r.append(i-a[i])

count = collections.Counter(r)
ans = 0
for i in l:
  ans += count.get(i,0)
      
print(ans)