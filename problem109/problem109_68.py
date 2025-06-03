num = int(input())

ac = 0
wa = 0
tle = 0
re = 0

for i in range(num):
    k = input()
    if k == "AC":
        ac += 1
    elif k == "WA":
        wa += 1
    elif k == "TLE":
        tle += 1
    elif k == "RE":
        re += 1

print("AC x " + str(ac))
print("WA x " + str(wa))
print("TLE x " + str(tle))
print("RE x " + str(re))