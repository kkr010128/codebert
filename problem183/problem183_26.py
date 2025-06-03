def make_divisors(n: int):
    lower_divs = []
    upper_divs = []
    i = 1
    while i**2 <= n:
        if n % i == 0:
            lower_divs.append(i)
            if i != n // i:
                upper_divs.append(n // i)
        i += 1
    return lower_divs + upper_divs[::-1]


n = int(input())
ans = len(make_divisors(n - 1)) - 1
for x in make_divisors(n)[1:]:
    if x == 1:
        continue
    z = n
    while z % x == 0:
        z = z // x
    z = z % x
    if z == 1:
        ans += 1

print(ans)
