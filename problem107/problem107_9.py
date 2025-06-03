def pop_count(n):
    return bin(n).count("1")


def f(n):
    if n == 0:
        return 0
    return f(n % pop_count(n)) + 1


N = int(input())
X = list(map(int, input()))
X_m = 0
X_p = 0
pop_X = X.count(1)
for i in range(N):
    if X[i] == 0:
        continue
    X_p += pow(2, N - i - 1, pop_X + 1)
    X_p %= pop_X + 1
    if pop_X > 1:
        X_m += pow(2, N - i - 1, pop_X - 1)
        X_m %= pop_X - 1

for i in range(N):
    ans = 1
    if X[i] == 0:
        ans += f((X_p + pow(2, N - i - 1, pop_X + 1)) % (pop_X + 1))
    elif pop_X > 1:
        ans += f((X_m - pow(2, N - i - 1, pop_X - 1)) % (pop_X - 1))
    else:
        ans = 0
    print(ans)
