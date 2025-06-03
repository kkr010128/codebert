import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


t1, t2 = list(map(int, sys.stdin.buffer.readline().split()))
a1, a2 = list(map(int, sys.stdin.buffer.readline().split()))
b1, b2 = list(map(int, sys.stdin.buffer.readline().split()))

da1 = t1 * a1
da2 = t2 * a2
db1 = t1 * b1
db2 = t2 * b2
if da1 + da2 > db1 + db2:
    a1, b1 = b1, a1
    a2, b2 = b2, a2
    da1, db1 = db1, da1
    da2, db2 = db2, da2
# b のほうがはやい

# 無限
if da1 + da2 == db1 + db2:
    print('infinity')
    exit()
# 1回も会わない
if da1 < db1:
    print(0)
    exit()

# t1 で出会う回数
cnt = abs(da1 - db1) / abs(da1 + da2 - db1 - db2)
ans = int(cnt) * 2 + 1
if cnt == int(cnt):
    ans -= 1
print(ans)
