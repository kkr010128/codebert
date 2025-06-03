l = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
s = input()
for i, day in enumerate(l):
    if day == s:
        if i == 0:
            print(7)
        else:
            print(7-i)