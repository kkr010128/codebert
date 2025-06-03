N, M = map(int, input().split())
ac = [False] * N
wa_cnt = [0] * N
ac_cnt = 0
for i in range(M):
    p, s = input().split()
    p_i = int(p) - 1
    if s == 'WA':
        if not ac[p_i]:
            wa_cnt[p_i] += 1
    else:
        if not ac[p_i]:
            ac[p_i] = True
            ac_cnt += 1

wa_cnt_sum = 0
for i in range(N):
    if ac[i]:
        wa_cnt_sum += wa_cnt[i]

print(ac_cnt,wa_cnt_sum)
