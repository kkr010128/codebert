n=int(input())
a=[0,1,2,0,4,0,0,7,8,0,0,11,0,13,14]
s=0
for i in range(n+1):
  if a[i%15]!=0:
    s+=a[i%15]+i//15*15
print(s)