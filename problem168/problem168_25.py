summer_vacation, amount_of_homework = map(int, input().split())
a = map(int, input().split())
homework_list = list(a)

total_days = 0

for i in homework_list:
    total_days += i

if summer_vacation >= total_days:
    print(summer_vacation - total_days)
else:
    print(-1)
