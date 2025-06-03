import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
X = input()
pc = X.count("1")

if pc == 1:
    if X[-1] == "0":
        for i, s in enumerate(X):
            if i == N - 1:
                print(2)
            elif s == "0":
                print(1)
            else:
                print(0)
    else:
        ans = [2] * (N - 1) + [0]
        print(*ans, sep="\n")
    exit()


m01 = 0
m10 = 0
b01 = 1
b10 = 1
for i, s in enumerate(X[::-1]):
    if s == "1":
        m01 += b01
        m01 %= pc + 1
        m10 += b10
        m10 %= pc - 1
    b01 *= 2
    b01 %= pc + 1
    b10 *= 2
    b10 %= pc - 1


def pop_count(T):
    T = (T & 0x55555555) + ((T >> 1) & 0x55555555)
    T = (T & 0x33333333) + ((T >> 2) & 0x33333333)
    T = (T & 0x0F0F0F0F) + ((T >> 4) & 0x0F0F0F0F)
    T = (T & 0x00FF00FF) + ((T >> 8) & 0x00FF00FF)
    T = (T & 0x0000FFFF) + ((T >> 16) & 0x0000FFFF)
    return T


memo = [0] * (N + 10)
for i in range(1, N + 10):
    p = pop_count(i)
    memo[i] = memo[i % p] + 1


ans = [0] * N
b01 = 1
b10 = 1
for i, s in enumerate(X[::-1]):
    if s == "0":
        m = m01
        m += b01
        m %= pc + 1
    else:
        m = m10
        m -= b10
        m %= pc - 1
    ans[i] = memo[m] + 1
    b01 *= 2
    b01 %= pc + 1
    b10 *= 2
    b10 %= pc - 1

print(*ans[::-1], sep="\n")