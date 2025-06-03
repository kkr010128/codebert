S = input()

day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
for i in range(len(day)):
  if S == day[i]:
    print(7-i)
    break