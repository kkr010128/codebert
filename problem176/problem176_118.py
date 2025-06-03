n,k=map(int,input().split())
A=[0]*k
mod=10**9+7

def power(a,x): #a**xの計算
    T=[a]
    while 2**(len(T))<mod: #a**1,a**2.a**4,a**8,...を計算しておく
        T.append(T[-1]**2%mod)
    b=bin(x) #xを2進数表記にする
    ans=1
    for i in range(len(b)-2):
        if int(b[-i-1])==1:
            ans=ans*T[i]%mod
    return ans

for i in range(k):
    cnt=power(k//(k-i),n)
    now=(k-i)*2
    while now<=k:
        cnt-=A[now-1]
        now+=k-i
    A[k-i-1]=cnt

ans=0
for i in range(k):
    ans+=(i+1)*A[i]%mod
    ans%=mod
print(ans)