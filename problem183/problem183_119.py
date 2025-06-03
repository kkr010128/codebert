def divisor(i):
    s = []
    for j in range(1, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            s.append(i // j)
            s.append(j)
    return sorted(set(s))

n = int(input())
ans = 0
d = divisor(n)
d.pop(0)
for i in d:
    x = n
    while True:
        if not x % i == 0:
            break
        x //= i
    if x % i == 1:
        ans += 1
d = divisor(n - 1)
ans += len(d)
ans -= 1
print(ans)