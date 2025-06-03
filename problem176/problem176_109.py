n,k=map(int,input().split())
# 1以上k以下の整数がn個
mod=int(1e+9 + 7)
d=[0]*(k+1)
ans=0
for i in range(k,0,-1):
      m=k//i
      d[i]=pow(m,n, mod) 
      d[i]-=sum([d[j*i]for j in range(2,m+1)])
      ans+=(d[i]*i)%mod
print((ans)%mod)
#print(d)

