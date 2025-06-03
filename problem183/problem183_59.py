def make_divisors(n):
    lsls=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            lsls.append(i)
            if i!=n//i:
                lsls.append(n//i)
    lsls.sort()
    return lsls

N=int(input())

ans=1
for K in range(2,min(N,int(N**0.5)+2)):
    num=N
    while num%K==0:
        num//=K
    if num>=K:
        num%=K
    if num==1:
        ans+=1

lst=make_divisors(N-1)

for u in lst:
    if u>=int(N**0.5)+2:
        ans+=1
        
print(ans)