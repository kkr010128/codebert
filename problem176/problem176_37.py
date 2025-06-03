n,k=map(int,input().split())
mod=pow(10,9)+7
ans=[0]*(k+1)
# gcdがkiとなる数列。すべてがkiの倍数でかつ少なくとも一つkiを含む
for ki in range(k,0,-1):
    a=k//ki
    ans[ki]=pow(a,n,mod)
    i=2
    while i*ki<=k:
        ans[ki]-=ans[i*ki]
        i+=1
b=0
for ki in range(1,k+1):
    b+=(ans[ki]*ki)%mod
    b%=mod
print(b)
