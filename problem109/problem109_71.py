n = int(input())
l = [input() for i in range(n)]
d = {k: 0 for k in ['AC', 'WA', 'TLE', 'RE']}
for s in l:
    d[s] += 1
for s in ['AC', 'WA', 'TLE', 'RE']:
    print('{} x {}'.format(s, d[s]))