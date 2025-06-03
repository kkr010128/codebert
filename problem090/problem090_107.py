weatherS = input()
serial = 0
dayBefore = ''
for x in weatherS:
    if dayBefore != 'R':
        if x == 'R':
            serial = 1
    else:
        if x == 'R':
            serial += 1
    dayBefore = x
print(serial)