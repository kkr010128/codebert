n = int(input())
a = [input() for i in range(n)]

c0, c1, c2, c3 = 0, 0, 0, 0

for output in a:
    if output == 'AC':
        c0 += 1
    elif output == 'WA':
        c1 += 1
    elif output == 'TLE':
        c2 += 1
    elif output == 'RE':
        c3 += 1
        
        
print('AC x {}'.format(c0))
print('WA x {}'.format(c1))
print('TLE x {}'.format(c2))
print('RE x {}'.format(c3))