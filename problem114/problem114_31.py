(d,), cc, *sstt = [list(map(int, s.split())) for s in open(0)]

ss = sstt[:d]

tt = list(map(lambda x: x-1, sum(sstt[d:], [])))

comp = [0]*len(cc)

ans = 0

for i in range(d):
    comp = [sum(x) for x in zip(comp, cc)]
    t = tt[i]
    ans += ss[i][t]
    comp[t] = 0
    ans -= sum(comp)
    print(ans)