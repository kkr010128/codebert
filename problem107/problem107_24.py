n = int(input())
x = list(map(int, input()))

one_cnt = x.count(1)
mods = [one_cnt - 1, one_cnt + 1]
sms = [0, 0]

for i in range(2):
    if mods[i] == 0:
        continue

    for j, e in enumerate(x):
        sms[i] += pow(2, n - j - 1, mods[i]) * e
        sms[i] %= mods[i]

for i, e in enumerate(x):
    idx = 1 - e
    mod = mods[idx]
    sm = sms[idx]

    if mod == 0:
        print(0)
        continue

    sm_changed = sm + pow(2, n - i - 1, mod) * (-1) ** e
    sm_changed %= mod
    ans = 1
    while sm_changed:
        tmp = sm_changed
        cnt = 0
        while tmp:
            cnt += tmp & 1
            tmp >>= 1

        sm_changed %= cnt
        ans += 1

    print(ans)
