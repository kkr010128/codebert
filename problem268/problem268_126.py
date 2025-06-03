mod = 10 ** 9 + 7

n = int(input())
a = map(int, input().split())

cnt = [0] * (n + 1)
cnt[-1] = 3

ret = 1
for x in a:
    ret = ret * cnt[x - 1] % mod
    cnt[x - 1] -= 1
    cnt[x] += 1

print(ret)
