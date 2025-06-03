x=int(input())
def divisors(n):
    lower_divisors=[]
    upper_divisors=[]
    i=1
    while i*i<=n:
        if n%i==0:
            lower_divisors.append(i)
            if i!=n//i:
                upper_divisors.append(n//i)
        i+=1
    return lower_divisors
max_lower_div=max(divisors(x))
print((max_lower_div-1)+(x//max_lower_div-1))