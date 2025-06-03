# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_e
# https://matsu7874.hatenablog.com/entry/2019/12/01/230357

n = int(input())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7
ans = 1

# 先頭はr/g/b
count = [3 if i == 0 else 0 for i in range(n + 1)]

for a in A:
    ans = ans * count[a] % MOD
    if ans == 0:
        break
    count[a] -= 1
    count[a + 1] += 1

print(ans)