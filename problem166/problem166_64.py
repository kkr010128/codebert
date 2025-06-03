from collections import Counter
S = list(input())
S.reverse()
MOD = 2019

t = [0]
r = 1
for i in range(len(S)):
    q = (t[-1] + (int(S[i]) * r)) % MOD
    t.append(q)
    r *= 10
    r %= MOD

cnt = Counter(t)
cnt_mc = cnt.most_common()

ans = 0
for _, j in cnt_mc:
    if j >= 2:
        ans += j * (j - 1) // 2
        
print(ans)