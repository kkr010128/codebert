n=int(input())
a=[]
for i in range(1,int(n**(1/2))+1):
  if n%i==0:
    a.append(i)
    a.append(int(n/i))
print(a[-1]+a[-2]-2 if len(a)%2==0 else a[-1]*2-2)