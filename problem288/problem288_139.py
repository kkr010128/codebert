N = int(input())
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
yakusulist = make_divisors(N)
center1 = yakusulist[(len(yakusulist)-1)//2]
center2 = yakusulist[(len(yakusulist))//2]
print(center1+center2-2)