N, M = [int(n) for n in input().split()]
solved = {}
result = {}

for i in range(M):
    p, S = input().split()
    status = result.setdefault(p, [])
    if len(status)==0:
        result[p] = []
        solved[p] = False
    if S == 'AC':
        solved[p] = True
    result[p].append(S)

ans = 0
wa = 0
for k, v in solved.items():
    if v:
        ans += 1
        wa += result[k].index('AC')
print(ans , wa)
