n = int(input())
l = list(map(int,input().split()))
if len(l) < 3:
  print(0)
  exit()
count = 0
l = sorted(l)
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if l[i] != l[j] != l[k] and l[i]+l[j] > l[k]:
        count += 1
print(count)