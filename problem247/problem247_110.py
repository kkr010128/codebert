# 最大公約数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = [0] * N
for i in range(N):
    a = A[i]
    while a % 2 == 0:
        a = a // 2
        cnt[i] += 1
if len(set(cnt)) != 1:
    print(0)
    exit()

x = A[0] // 2
for a in A[1:]:
    x = lcm(x, a // 2)
ans = M // x
print(ans - ans // 2)