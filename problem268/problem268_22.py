from collections import defaultdict

p = 10 ** 9 + 7
n = int(input())
a = [int(x) for x in input().split()]

num = defaultdict(int)
num[-1] = 3
col = [None] * n
for i in range(n):
    col[i] = num[a[i] - 1]
    num[a[i]] += 1
    num[a[i] - 1] -= 1

ans = 1
for i in range(n):
    ans = ans * col[i] % p

print(ans)