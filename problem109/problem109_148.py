N = int(input())
status = []
for i in range(N):
    S = str(input())
    status.append(S)

print('AC x %d'% status.count("AC"))
print('WA x %d'% status.count('WA'))
print('TLE x %d'% status.count('TLE'))
print('RE x %d'% status.count('RE'))