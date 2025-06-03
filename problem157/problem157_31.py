import collections

n = int(input())
a = list(map(int, input().split()))

l = []
r = []
for i in range(n):
  l.append(i+a[i])
  r.append(i-a[i])

count_l = collections.Counter(l)
count_r = collections.Counter(r)

ans = 0
for i in count_l:
  ans += count_r.get(i,0) * count_l[i]
      
print(ans)