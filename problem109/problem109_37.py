N = int(input())

ac = 0
wa = 0
tle = 0
re = 0

for i in range(N):
    s = input()
    if s == 'AC':
        ac += 1
    elif s == 'WA':
        wa += 1
    elif s == 'TLE':
        tle += 1
    else:
        re += 1
t = [ac, wa, tle, re]        
for i in range(4):
    if i == 0:
        print('AC x ' + str(ac))
    if i == 1:
        print('WA x ' + str(wa))                    
    
    if i == 2:
        print('TLE x ' + str(tle))
    if i == 3:
        print('RE x ' + str(re))     