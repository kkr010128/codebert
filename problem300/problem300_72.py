a,b = map(int, input().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return False
    return True

ab = list(set(make_divisors(a)) & set(make_divisors(b)))

ans = 1
for i in ab[1:]:
    if is_prime(i): ans += 1
print(ans)