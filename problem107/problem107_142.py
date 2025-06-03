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
for i, s in enumerate(X[::-1]):
    if s == "1":
        m01 += pow(2, i, pc + 1)
        m01 %= pc + 1
        m10 += pow(2, i, pc - 1)
        m10 %= pc - 1


memo = [-1] * 200005


def pop_count(T):
    T = (T & 0x55555555) + ((T >> 1) & 0x55555555)
    T = (T & 0x33333333) + ((T >> 2) & 0x33333333)
    T = (T & 0x0F0F0F0F) + ((T >> 4) & 0x0F0F0F0F)
    T = (T & 0x00FF00FF) + ((T >> 8) & 0x00FF00FF)
    T = (T & 0x0000FFFF) + ((T >> 16) & 0x0000FFFF)
    return T


def F(n):
    if memo[n] != -1:
        return memo[n]
    if n == 0:
        return 0
    memo[n] = F(n % pop_count(n)) + 1
    return memo[n]


ans = [0] * N
for i, s in enumerate(X[::-1]):
    if s == "0":
        m = m01
        m += pow(2, i, pc+1)
        m %= pc + 1
    else:
        m = m10
        m -= pow(2, i, pc-1)
        m %= pc - 1
    ans[i] = F(m) + 1

print(*ans[::-1], sep="\n")
