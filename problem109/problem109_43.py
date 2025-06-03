N = int(input().rstrip())

A = []
for i in range(N):
  line = input().rstrip()
  A.append(line)
  
print('AC x', A.count('AC'))
print('WA x', A.count('WA'))
print('TLE x', A.count('TLE'))
print('RE x', A.count('RE'))