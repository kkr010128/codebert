H,N = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
reversed(a)
flag = True
for i in range(N):
  H-=a[i]
  if H<=0:
    flag = False
    print('Yes')
    break
if flag == True:
  print('No')