import itertools

def abc167c_skill_up():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for _ in range(n):
        v = list(map(int, input().split()))
        c.append(v[0])
        a.append(v[1:])
    pattern = itertools.product([0,1], repeat=n)
    best = float('inf')
    for p in pattern:
        cost = 0
        skill = [0] * m
        for i, v in enumerate(p):
            if v == 1:
                cost += c[i]
                if cost > best: break
                check = True
                for j in range(m):
                    skill[j] += a[i][j]
                    if skill[j] < x:
                        check = False
                if check:
                    best = cost
                    break
    if best == float('inf'):
        print('-1')
    else:
        print(best)
abc167c_skill_up()