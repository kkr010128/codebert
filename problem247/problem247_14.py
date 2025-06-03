def gcd(x, y):
    if x == 0:
        return y

    return gcd(y % x, x)


def lcm(x, y):
    return x // gcd(x, y) * y


n, m = map(int, input().split())
a = list(map(int, input().split()))

aa = [e // 2 for e in a]

for i, e in enumerate(aa):
    if i == 0:
        base = 0
        while e % 2 == 0:
            e //= 2
            base += 1

    else:
        cnt = 0
        while e % 2 == 0:
            e //= 2
            cnt += 1

        if cnt != base:
            print(0)
            exit()

c = 1
for e in aa:
    c = lcm(c, e)


ans = (m - c) // (2 * c) + 1
print(ans)
