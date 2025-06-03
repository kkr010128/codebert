n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=0

x=[0]+[True]*10**6

for i in range(len(a)):
  cnt=a[i]
  if x[a[i]]==True and (i==0 or a[i]!=a[i-1]) and (i==(n-1) or a[i]!=a[i+1]):
        ans+=1
        while cnt<=10**6:
          x[cnt]=False
          cnt+=a[i]
          
  elif x[a[i]]==True and ((i!=0 and a[i]==a[i-1]) or (i!=(n-1) and a[i]==a[i+1])):
        while cnt<=10**6:
          x[cnt]=False
          cnt+=a[i]
print(ans)
