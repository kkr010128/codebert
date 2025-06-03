n = int(input())
l = [0, 0, 0, 0]
for _ in range(n):
  s = input()
  if s == 'AC':
    l[0] += 1
  elif s == 'WA':
    l[1] += 1
  elif s == 'TLE':
    l[2] += 1
  else:
    l[3] += 1
print("AC x " + str(l[0]))
print("WA x " + str(l[1]))
print("TLE x " + str(l[2]))
print("RE x " + str(l[3]))