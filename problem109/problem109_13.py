N = int(input())
ac_counter = 0
wa_counter = 0
tle_counter = 0
re_counter = 0
for i in range(N):
    current = input()
    if current == 'AC':
        ac_counter += 1
    if current == 'WA':
        wa_counter += 1
    if current == 'TLE':
        tle_counter += 1
    if current == "RE":
        re_counter += 1
print("AC x " + str(ac_counter))
print("WA x " + str(wa_counter))
print("TLE x " + str(tle_counter))
print("RE x " + str(re_counter))

