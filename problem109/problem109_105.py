N = int(input())

AC = 0
WA = 0
TLE = 0
RE = 0

for i in range(N):
  ans = input()
  
  if ans == "AC":
    AC += 1
    
  elif ans == "WA":
    WA += 1
    
  elif ans == "TLE":
    TLE += 1
    
  elif ans == "RE":
    RE += 1
    
print("AC x", AC)
print("WA x", WA)
print("TLE x", TLE)
print("RE x", RE)
