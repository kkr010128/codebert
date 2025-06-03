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

def min2(x,y):
    return x if x < y else y

N = int(input())
P = make_divisors(N)
L = len(P) + 1
res =float("inf")

for p in P:
    res = min2((p - 1) + (N // p - 1), res)

print(res)