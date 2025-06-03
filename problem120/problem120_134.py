n,k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
c = 0
i = 0
while i < k:
  c += l[i]
  i += 1
print(c)