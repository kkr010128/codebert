N=int(input())
n=N
ans=0
def make_divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)

    return divisors
l=make_divisors(N-1)
r=make_divisors(N)
ans=len(l)-1
for i in range(len(r)):
    N=n
    K=r[i]
    if K==1:
        continue
    while(N%K==0):
        N=N//K
    if N%K==1:
        #print(K)
        ans+=1
print(ans)