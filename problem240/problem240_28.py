n,m = map(int,input().split())
prb = [[0] for _ in range(n+1)]

for _ in range(m):
    sub = input().split()
    p, s = int(sub[0]), sub[1]
    lst = prb[p]
    if lst[-1] == 1:
        pass
    elif s == "WA":
        lst.append(0)
    elif s == "AC":
        lst.append(1)
    prb[p] = lst

ac_prb = [lst for lst in prb if lst[-1] == 1]
ac_num = len(ac_prb)
pe_num = -2*ac_num

for prb in ac_prb:
    pe_num += len(prb)

print(ac_num, pe_num)