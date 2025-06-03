n, m = map(int, input().split())
ans_dict = {}
for _ in range(m):
    p, s = input().split()
    if p not in ans_dict:
        ans_dict[p] = [s]
    else:
        ans_dict[p].append(s)

ac_cnt = 0
wa_cnt = 0

ac_ans = 0
wa_ans = 0

for key in ans_dict.keys():
    ac_cnt = ans_dict[key].count('AC')
    wa_cnt = ans_dict[key].count('WA')
    if ac_cnt != 0:
        ac_ans += 1
        # その問題の解答一覧で最初にACとなったインデックスを取得
        ac_index = ans_dict[key].index('AC')
        wa_ans += ans_dict[key][:ac_index].count('WA')
    
print(ac_ans, wa_ans) 