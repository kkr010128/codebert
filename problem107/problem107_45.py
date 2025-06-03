from functools import lru_cache


def popcnt(x):
    return bin(x).count("1")


@lru_cache(maxsize=None)
def rec(n):
    if n == 0:
        return 0
    else:
        return rec(n % popcnt(n)) + 1


n = int(input())
x = int(input(), 2)

# 事前計算
cnt = popcnt(x)
init_big = x % (cnt + 1)
if cnt == 1:
    init_small = 0
else:
    init_small = x % (cnt - 1)

# 差分計算
result = []
for i in range(n):
    if not (x >> i) & 1:
        result.append((init_big + pow(2, i, cnt + 1)) % (cnt + 1))
    elif x == 1 << i or cnt - 1 == 0:
        result.append("x")
    else:
        result.append((init_small - pow(2, i, cnt - 1)) % (cnt - 1))

ans = []
for x in result[::-1]:
    if x == "x":
        ans.append(0)
    else:
        ans.append(rec(x) + 1)

print(*ans, sep="\n")