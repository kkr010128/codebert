n,k = map(int,input().split())
p = map(int,input().split())
p = sorted(p)
total = 0
for i in range(k):
  total += p[i]
print(total)
