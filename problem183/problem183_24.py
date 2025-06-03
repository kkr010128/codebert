
def calc_divisor(x):
    divisor = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divisor.append(i)
            if i != x // i:
                divisor.append(x // i)
    return divisor


N = int(input())
ans = len(calc_divisor(N - 1)) - 1

cand = sorted(calc_divisor(N))[1:]
for k in cand:
    x = N
    while x % k == 0:
        x //= k
    if x % k == 1:
        ans += 1

print(ans)
