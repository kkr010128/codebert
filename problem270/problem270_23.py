days = ('SUN','MON','TUE','WED','THU','FRI','SAT')
Day_of_the_week = input()

for index, day in enumerate(days):
    if Day_of_the_week == day:
        print(7 - index)