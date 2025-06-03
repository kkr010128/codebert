wd = ['SUN','MON','TUE','WED','THU','FRI','SAT']
s = input()

print(str(7 - wd.index(s) % 7))