def report(k, r):
    print('{} x {}'.format(k, r[k]))

ans = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}

N = int(input().rstrip())
for i in range(N):
    S = input().rstrip()
    ans[S] += 1

report('AC', ans)
report('WA', ans)
report('TLE', ans)
report('RE', ans)
