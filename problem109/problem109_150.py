N = int(input())
C_0 = 0
C_1 = 0
C_2 = 0
C_3 = 0
for _ in range(N):
    S = input()
    if S == 'AC':
        C_0 += 1
    elif S == 'WA':
        C_1 += 1
    elif S == 'TLE':
        C_2 += 1
    else:
        C_3 += 1
print('AC x {}'.format(C_0))
print('WA x {}'.format(C_1))
print('TLE x {}'.format(C_2))
print('RE x {}'.format(C_3))
