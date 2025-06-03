week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
S = input()

print(6 - week.index(S)) if week.index(S) != 6 else print(7)