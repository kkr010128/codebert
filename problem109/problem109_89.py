N = int(input())
S = [input() for _ in range(N)]
C0 = 0
C1 = 0
C2 = 0
C3 = 0
for i in range(N):
  if S[i] == "AC": C0 += 1
  elif S[i] == "WA": C1 += 1
  elif S[i] == "TLE": C2 += 1
  else: C3 += 1
print("AC x "+ str(C0))
print("WA x "+ str(C1))
print("TLE x "+ str(C2))
print("RE x "+ str(C3))
