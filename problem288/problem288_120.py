import itertools
n = int(input())

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

div_list = make_divisors(n)
#print(div_list)

mn =2**50
for i in div_list:
    mn = min(mn,i+n//i)

print(mn-2)