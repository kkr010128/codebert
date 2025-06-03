import fractions
import math

def divide_two(x):
    ans = 0
    while x > 0:
        if x % 2 == 0:
            ans += 1
            x = x // 2
        else:
            break
    return ans

n, m = map(int, input().split())
a = list(map(int, input().split()))
flag = [divide_two(i) for i in a]

if sum(flag) != flag[0] * n:
    ans = 0
else:
    # 最小公倍数求める
    lcm = a[0]
    for i in range(1, n):
        lcm = lcm * a[i] // fractions.gcd(lcm, a[i])

    ans = math.floor(m / lcm + 0.5)
print(ans)