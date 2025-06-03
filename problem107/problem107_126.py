
N = int(input())
X = input()

mod0 = X.count("1") + 1
mod1 = X.count("1") - 1

full0 = 0
full1 = 0
for i in range(N):
    if X[i] == "1":
        full0 = (full0 + pow(2, N - i - 1, mod0)) % mod0
        if mod1 > 0:
            full1 = (full1 + pow(2, N - i - 1, mod1)) % mod1

ans = [0] * N
for i in range(N):
    if X[i] == "0":
        cur = (full0 + pow(2, N - i - 1, mod0)) % mod0
        res = 1
    else:
        if mod1 > 0:
            cur = (full1 - pow(2, N - i - 1, mod1)) % mod1
            res = 1
        else:
            cur = 0
            res = 0

    while cur > 0:
        cur %= bin(cur).count("1")
        res += 1
    ans[i] = res

print(*ans, sep="\n")
