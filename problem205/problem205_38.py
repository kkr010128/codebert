from collections import Counter


N, P = map(int, input().split())
S = list(input())

cnt = 0
if P in [2, 5]:
    for i, s in enumerate(S):
        if int(s) % P == 0:
            cnt += (i + 1)
else:
    num = 0
    mods = Counter()
    for i, s in enumerate(reversed(S)):
        num += int(s) * pow(10, i, P)
        num %= P
        mods[num] += 1
    mods[0] += 1
    for i, s in enumerate(S):
        mods[num] -= 1
        cnt += mods[num]
        num -= int(s) * pow(10, N - 1 - i, P)
        num %= P

print(cnt)
