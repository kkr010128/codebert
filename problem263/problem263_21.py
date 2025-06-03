mod = 10**9 + 7
n = int(input())
dat = list(map(int, input().split()))
cnt0 = [0] * 64
cnt1 = [0] * 64
for i in range(n):
    for j in range(62):
        if ((dat[i] >> j) & 1) == 1:
            cnt1[j] += 1
        else:
            cnt0[j] += 1
#print(cnt0)
#print(cnt1)
res = 0
for i in range(62):
    res += (cnt0[i] * cnt1[i]) << i
    res %= mod
print(res)