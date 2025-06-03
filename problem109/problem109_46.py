N=int(input())
S = [0]*N
for i in range(N):
    S[i]=str(input())
    
print('AC x {0}'.format(S.count('AC')))
print('WA x {0}'.format(S.count('WA')))
print('TLE x {0}'.format(S.count('TLE')))
print('RE x {0}'.format(S.count('RE')))