N, P = map(int, input().split())
S = [int(x) for x in input()]
if P == 2:
    ans = 0
    for i in range(N):
        if S[N-1-i] % 2 == 0:
            ans += N-i
elif P == 5:
    ans = 0
    for i in range(N):
        if S[N-1-i] % 5 == 0:
            ans += N-i
else:
    ans = 0
    cnt = [0] * P
    cnt[0] = 1
    dec_mod, pre_mod = 1, 0
    for i in range(N):
        mod = (S[N-1-i] * dec_mod + pre_mod) % P
        ans += cnt[mod]
        cnt[mod] += 1
        dec_mod = dec_mod * 10 % P
        pre_mod = mod
print(ans)
