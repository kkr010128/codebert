SN=[5,1,2,6]
WE=[4,1,3,6]

def EWSN(d):
  global SN,WE
  if d == "S" :
    SN = SN[3:4] + SN[0:3]
    WE[3] = SN[3]
    WE[1] = SN[1]
  elif d == "N":
    SN = SN[1:4] + SN[0:1]
    WE[3] = SN[3]
    WE[1] = SN[1]
  elif d == "E":
    WE = WE[3:4] + WE[0:3]
    SN[3] = WE[3]
    SN[1] = WE[1]
  elif d == "W":
    WE = WE[1:4] + WE[0:1]
    SN[3] = WE[3]
    SN[1] = WE[1]

dice = list(map(int,input().split(" ")))
op = input()

for i in op:
  EWSN(i)
print(dice[SN[1] - 1])
