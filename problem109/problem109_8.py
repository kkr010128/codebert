n = int(input())
ACs = 0
WAs = 0
TLEs = 0
REs = 0
for i in range(n):
  result = input()
  if result == "AC":
    ACs += 1
  elif result == "WA":
    WAs += 1
  elif result == "TLE":
    TLEs += 1
  else:
    REs += 1
print("AC x " + str(ACs))
print("WA x " + str(WAs))
print("TLE x " + str(TLEs))
print("RE x " + str(REs))
