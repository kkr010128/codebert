n=int(input())
a=list(map(int,input().split()))

ans=1

d={}

ch=0

mod=10**9+7

for i in range(n):
  if a[i]==0:
    if 0 not in d:
      d[0]=1
      ans*=3
    else:
      if d[0]==1:
        d[0]=2
        ans*=2
      elif d[0]==2:
        d[0]=3
      else:
        ch+=1
        break
      
  else:
    if a[i] not in d:
      d[a[i]]=1
      if a[i]-1 not in d:
        ch+=1
        break
      else:
        ans*=d[a[i]-1]
    else:
      if d[a[i]]==1:
        d[a[i]]=2
        if a[i]-1 not in d:
          ch+=1
          break
        else:
          if d[a[i]-1]>=2:
            ans*=d[a[i]-1]-1
          else:
            ch+=1
            break
      elif d[a[i]]==2:
        d[a[i]]=3
        if a[i]-1 not in d:
          ch+=1
          break
        else:
          if d[a[i]-1]>=3:
            ans*=1
          else:
            ch+=1
            break
      else:
        ch+=1
        break
        
  ans=(ans%mod)
  
if ch==0:
  print(ans)
else:
  print(0)


