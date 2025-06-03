n, m = map(int, input().split())
s = [[] for i in range(n)]
for i in range(m):
    p, S = input().split()
    s[int(p) - 1] += [S]
print(sum('AC' in si for si in s), end=' ')
print(sum(si[:si.index('AC')].count('WA') if 'AC' in si else 0 for si in s))