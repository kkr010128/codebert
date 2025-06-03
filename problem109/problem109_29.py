N = int(input())
S = [input() for i in range(N)]
c0, c1, c2, c3 = 0, 0, 0, 0
for i in S:
    if i == 'AC':
        c0 += 1 
    if i == 'WA':
        c1 += 1
    if i == 'TLE':
        c2 += 1
    if i == 'RE':
        c3 += 1
print('AC','x',c0)
print('WA','x',c1)
print('TLE','x',c2)
print('RE','x',c3)