n, m = map(int, input().split())
if m > 0:
    p, s = zip(* [input().split() for _ in range(m)])
else:
    p = []
    s = []

ac_dict = {str(i): False for i in range(1, n + 1)}
wa_dict = {str(i): 0 for i in range(1, n + 1)}
ac_num = 0
wa_num = 0
for p_i, s_i in zip(p, s):
    if ac_dict[p_i] == False:
        if s_i == 'AC':
            ac_num += 1
            wa_num += wa_dict[p_i]
            ac_dict[p_i] = True
        elif s_i == 'WA':
            wa_dict[p_i] += 1
print('{} {}'.format(ac_num, wa_num))
