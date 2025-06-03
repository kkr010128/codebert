weekday = ['SUN', 'SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON']
val = input()
if val == 'SUN':
    print("7")
else:
    print(weekday.index(val))