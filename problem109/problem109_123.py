n = int(input())

cnt_ac = 0
cnt_wa = 0
cnt_tle = 0
cnt_re = 0

for i in range(n):
    s = input()
    if s == 'AC':
        cnt_ac += 1
    elif s == 'WA':
        cnt_wa += 1
    elif s == 'TLE':
        cnt_tle += 1
    elif s == "RE":
        cnt_re += 1

print('AC x ', cnt_ac)
print('WA x ', cnt_wa)
print('TLE x ', cnt_tle)
print('RE x ', cnt_re)


