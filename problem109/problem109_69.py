n = int(input())
count_ac, count_wa, count_tle, count_re = 0, 0, 0, 0
for i in range(n):
    s = input()
    if s == "AC":
        count_ac += 1
    if s == "WA":
        count_wa += 1
    if s == "TLE":
        count_tle += 1
    if s == "RE":
        count_re += 1

print("AC x", count_ac)
print("WA x", count_wa)
print("TLE x", count_tle)
print("RE x", count_re)