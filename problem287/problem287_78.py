N=int(input())
ok=0
for i in range(1,10):
  j = N/i
  if j==int(j) and 1<=j<=9:
    ok=1
    print('Yes')
    break
if ok==0:print('No')