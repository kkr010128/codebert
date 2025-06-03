N = int(input())
S = [input() for _ in range(N)]

AC = 0
WA = 0
TLE = 0
RE = 0

for i in S:
    if i == 'AC':
        AC += 1
    elif i == 'WA':
        WA += 1
    elif i == 'TLE':
        TLE += 1
    else:
        RE += 1
        
print('AC x', AC)
print('WA x', WA)
print('TLE x', TLE)
print('RE x', RE)