import itertools
n, m = [int(w) for w in input().split()]

wa_n = [0] * n
ac_n = [0] * n

for i in range(m):
    p, s = input().split()
    p = int(p) - 1
    if s == "AC":
        ac_n[p] = 1
    else:
        if ac_n[p] == 1:
            continue
        else:
            wa_n[p] += 1


print(sum(ac_n), sum(list(itertools.compress(wa_n, ac_n))))
