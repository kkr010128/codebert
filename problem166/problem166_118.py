from collections import defaultdict

S = input()
kTarget = 2019

mod2cnt = defaultdict(int)
mod2cnt[0] += 1

ord_z = ord('0')
res = 0
for i in range(len(S)-1, -1, -1):
    d = ord(S[i]) - ord_z
    res = (res+d*pow(10, len(S)-1-i, kTarget))%kTarget
    mod2cnt[res] += 1

ans = 0
for cnt in mod2cnt.values():
    ans += cnt*(cnt-1)
print(ans//2)