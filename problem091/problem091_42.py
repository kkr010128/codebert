N=int(input())
L = list(map(int,input().split()))

ans = 0
if N<=2:
  print(0)
  exit()
for i1 in range(N-2):
  l1 = L[i1]
  for i2 in range(i1+1,N-1):
    l2 = L[i2]
    for i3 in range(i2+1,N):
      l3 = L[i3]
      if l1==l2 or l2==l3 or l3==l1: continue
      tmp = sorted([l1,l2,l3])
      if tmp[0]+tmp[1]>tmp[2]:
        ans += 1
print(ans)