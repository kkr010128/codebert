n,m = map(int,input().split())
ac_list = [0 for i in range(n+1)]
wa_list = [0 for i in range(n+1)]
p_list = []
ac = 0
pena = 0

for i in range(m):
    p,s = map(str,input().split())
    p = int(p)
    if s == 'AC' and ac_list[p-1] != 1:
        ac += 1
        ac_list[p-1] = 1
        pena += wa_list[p-1]
    elif s == 'WA' and ac_list[p-1] != 1:
        wa_list[p-1] += 1

print(ac, pena)
