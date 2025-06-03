import fractions

A, B = list(map(int, input().split()))

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

l = sorted(list(set(make_divisors(A)) & set(make_divisors(B))))
#print(l)
i = 0
while i < len(l):
    v = l[i]
    if v == 1:
        i += 1
        continue
    l = l[0:i+1] + list(filter(lambda x: x % v != 0, l[i+1:]))
#    print(l)
    i += 1
print(len(l))
