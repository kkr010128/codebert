a = 0
b = 0
c = 0
d = 0
N = int(input())
S = []
for i in range(N):
    S.append(input())
for j in range(N):
  if S[j] == 'AC':
    a += 1
  elif S[j] == 'WA':
    b += 1
  elif S[j] == 'TLE':
    c += 1
  elif S[j] == 'RE':
    d += 1
print('AC x', a)
print('WA x', b)
print('TLE x', c)
print('RE x', d)