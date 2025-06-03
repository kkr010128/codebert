n = int(input())
p= []
AC = 0
WA = 0
TLE = 0
RE = 0
 
for i in range(n):
  p.append(input())
  
for j in p :
  if j == "AC":
    AC += 1
  elif j == "WA":
    WA += 1
  elif j == "TLE":
    TLE += 1
  else:
    RE += 1


  
print("AC x " + str(AC))
print("WA x " + str(WA))
print("TLE x " + str(TLE))
print("RE x " + str(RE))