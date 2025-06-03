n=int(input())
a=[int(x) for x in input().rstrip().split()]

now=1
cnt=0
for i in range(n):
  if now==a[i]:
    now+=1
  else:
    cnt+=1

if n==cnt:
  print(-1)
else:
  print(cnt)
