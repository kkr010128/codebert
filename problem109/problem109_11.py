N = int(input())
c = [0]*4
for i in range(N):
    s = input()
    if s == 'AC':
        c[0] += 1
    elif s == 'WA':
        c[1] += 1
    elif s == 'TLE':
        c[2] += 1
    else:
        c[3] += 1
print('AC x ',c[0])
print('WA x ',c[1])
print('TLE x ',c[2])
print('RE x ',c[3])
