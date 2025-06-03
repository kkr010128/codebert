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

X = int(input())
S = make_divisors(X)

t = 0
for s in S:
    a = s//2
    b = a-s
    while a**5 - b**5 <= X:
        if a**5 - b**5 == X:
            print(a,b)
            break
        a += 1
        b += 1
    if a**5 - b**5 == X:
        break