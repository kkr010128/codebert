n=int(input())
a=list(map(int,input().split()))
l=[3]+[0]*(10**5)
m=10**9+7
x=1
for i in a:
  if l[i]:
    x=(x*l[i])%m
    l[i]-=1
    l[i+1]+=1
  else:
    x=0
    break
print(x)