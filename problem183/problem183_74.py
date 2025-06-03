N=int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return(divisors)

l1=make_divisors(N)
ans=len(make_divisors(N-1))-1

for i in l1:
    m=N
    while m%i==0 and m!=1 and m!=0 and i!=1:
        m//=i
    if m%i==1:
        ans+=1

print(ans)