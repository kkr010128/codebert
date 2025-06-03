n = int(input())
ac = 0
wa = 0
tle = 0
re = 0
for i in range(n):
  x = input()
  if (x == "AC"):
    ac = ac + 1
  elif (x == "WA"):
    wa = wa + 1
  elif (x == "TLE"):
    tle = tle + 1
  else:
    re = re + 1
print("AC", "x", ac)
print("WA", "x", wa)
print("TLE", "x", tle)
print("RE", "x", re)