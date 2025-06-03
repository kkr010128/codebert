days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

current_day = input()

i = 0

while True:
    if days[i] == current_day:
        break
    i += 1

print(7 - i)