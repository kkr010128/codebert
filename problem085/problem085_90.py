def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,a%b)

n=int(input())
arr=list(map(int,input().split()))
g=arr[0]
cnt=[0]*(10**6+1)
for val in arr:
  g=gcd(g,val)
  cnt[val]+=1
for i in range(2,10**6+1):
  tmp=0
  for j in range(i,10**6+1,i):
    tmp+=cnt[j]
  if tmp>=2:
    break
if i==10**6:
  print('pairwise coprime')
elif g==1:
  print('setwise coprime')
else:
  print('not coprime')