N = int(input())
S = []
for _ in range(N):
    S.append(input())
    
ac = 0
wa = 0
tle = 0
re = 0
for s in S:
    if s == "AC":
        ac += 1
    if s == "WA":
        wa += 1
    if s == "TLE":
        tle += 1
    if s == "RE":
        re += 1

print("AC x ",ac)
print("WA x ",wa)
print("TLE x ",tle)
print("RE x ",re)