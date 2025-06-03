y = ['SUN','MON','TUE','WED','THU','FRI','SAT']
s = input()
for i, j in enumerate(y):
    if s == j:
        print(7-i)
        exit()