n = int(input())
s = []
for _ in range(n):
    s.append(str(input()))
print('AC x ' + str(s.count('AC')))
print('WA x ' + str(s.count('WA')))
print('TLE x ' + str(s.count('TLE')))
print('RE x ' + str(s.count('RE')))