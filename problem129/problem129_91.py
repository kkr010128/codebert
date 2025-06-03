counter = [0 for i in range(10**6+1)]
n = int(input())
a = sorted(list(map(int,input().split())))
for i in a:
  counter[i] += 1
l  = [0 for i in range(10**6+1)]
cou = 0
for i in range(n):
  b = a[i]
  if l[b]==0:
    cou += 1
    for j in range(b,10**6+1,b):
      l[j] = 1
    if counter[b]>=2:
      cou -=1
print(cou)