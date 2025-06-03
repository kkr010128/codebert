n = int(input())
c0, c1, c2, c3 = 0, 0, 0, 0

for i in range(n):
    s = input()
    if s == 'AC':
        c0 += 1
    elif s == 'WA':
        c1 += 1
    elif s == 'TLE':
        c2 += 1
    else:
        c3 += 1

print('AC x',c0)
print('WA x',c1)
print('TLE x',c2)
print('RE x',c3) 
