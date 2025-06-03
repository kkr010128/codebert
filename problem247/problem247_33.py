def GCD(x, y):
    if y == 0:
        return x
    return GCD(y, x % y)


N, M = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(set(A))

check = set()
for a in A:
    cnt = 0
    while a % 2 == 0:
        cnt += 1
        a //= 2
    check.add(cnt)

if len(check) > 1:
    print(0)
    exit()

LCM = 1
for a in A:
    gcd = GCD(LCM, a // 2)
    LCM = LCM * (a // 2) // gcd

ans = (M - LCM) // (2 * LCM) + 1
print(ans)