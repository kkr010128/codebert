s = input()[::-1]

MOD = 2019

cum = 0
cnt = [0] * 2019
cnt[0] = 1

d = 1
for c in s:
    cum += int(c) * d
    cum %= MOD
    cnt[cum] += 1
    d *= 10
    d %= MOD

ans = 0
for v in cnt:
    ans += v * (v - 1) // 2

print(ans)
