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

n = int(input())
divisors = make_divisors(n)
#print(divisors)
if len(divisors)%2==1:
    print(divisors[len(divisors)//2]*2-2)
else:
    m = len(divisors)//2
    print(divisors[m-1]+divisors[m]-2)