def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
    
n=int(input())
lis=make_divisors(n)
#print(lis)
ans=float('inf')
l=len(lis)
for i in range(l//2):
    ans=min(ans,lis[i]+lis[-1*(i+1)]-2)
if l%2:
    ans=min(ans,2*(lis[l//2]-1))
print(ans)