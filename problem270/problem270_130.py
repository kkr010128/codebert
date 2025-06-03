day = ['','SAT','FRI','THU','WED','TUE','MON','SUN']
s = str(input())
for i in range(8):
    if s==day[i]:
        break
print(i)