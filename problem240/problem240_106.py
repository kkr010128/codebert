from collections import defaultdict

n, m = map(int, input().split())
ac_dict = defaultdict(int)
wa_dict = defaultdict(int)
ac_p, wa_p = set(), set()
for _ in range(m):
    p, s = input().split()
    p = int(p)
    if s == 'AC':
        ac_p.add(p)
        ac_dict[p] = 1
    elif ac_dict[p] != 1:
        wa_p.add(p)
        wa_dict[p] += 1

wa = 0
for pi in ac_p:
    wa += wa_dict[pi]

print(sum(ac_dict.values()), wa)
