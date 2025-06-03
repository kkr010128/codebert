n = int(input())
AC = 0
WA = 0
TLE = 0
RE = 0
for i in range(n):
    x = input()
    if x == "AC":
        AC += 1
    elif x == "WA":
        WA += 1
    elif x == "TLE":
        TLE += 1
    elif x == "RE":
        RE += 1
print("AC x " + str(AC))
print("WA x " + str(WA))
print("TLE x " + str(TLE))
print("RE x " + str(RE))
