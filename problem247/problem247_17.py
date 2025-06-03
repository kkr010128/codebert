from fractions import gcd


def count(x):
    ans = 0
    while x % 2 == 0:
        ans += 1
        x = x // 2
    return ans


N, M = map(int, input().split(' '))
a = list(map(lambda x: int(x) // 2, input().split(' ')))

lcm, div2 = a[0], count(a[0])
flag = True

for i in range(1, N):
    lcm = lcm // gcd(lcm, a[i]) * a[i]
    if count(a[i]) != div2:
        flag = False

if flag:
    print((M // lcm + 1) // 2)
else:
    print(0)