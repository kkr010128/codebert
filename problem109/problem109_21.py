n = int(input())
c0 = 0
c1 = 0
c2 = 0
c3 = 0
for _ in range(n):
  s = input()
  if s == 'AC':
    c0 += 1
  elif s == 'WA':
    c1 += 1
  elif s == 'TLE':
    c2 += 1
  elif s == 'RE':
    c3 += 1
print('AC x', c0)
print('WA x', c1)
print('TLE x', c2)
print('RE x', c3)