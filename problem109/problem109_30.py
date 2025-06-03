#B
N=int(input())
C=[input() for i in range(N)]
AC=C.count('AC')
WA=C.count('WA')
TLE=C.count('TLE')
RE=C.count('RE')
print('AC x {}\nWA x {}\nTLE x {}\nRE x {}'.format(AC, WA, TLE, RE))