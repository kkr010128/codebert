N = int(input())
ansAC = 0
ansWA = 0
ansTLE = 0
ansRE = 0
 
for i in range(N):
  S = input()
  if S == "AC":
    ansAC += 1
  elif S == "TLE":
    ansTLE += 1
  elif S == "WA":
    ansWA += 1
  elif S == "RE":
    ansRE += 1
print("AC x " + str(ansAC))
print("WA x " + str(ansWA))
print("TLE x " + str(ansTLE))
print("RE x " + str(ansRE))