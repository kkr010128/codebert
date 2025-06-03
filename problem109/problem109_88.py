Nin = int(input())
a = [input() for i in range(Nin)]

ac  = 0
wa  = 0
tle = 0
re  = 0

for i in range(Nin):
    if a[i] == "AC":
        ac += 1
    elif a[i] == "WA":
        wa += 1
    elif a[i] == "TLE":
        tle += 1
    elif a[i] == "RE":
        re += 1

print("AC x", ac)
print("WA x", wa)
print("TLE x", tle)
print("RE x", re)
