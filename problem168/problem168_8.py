days_summer_vacation, amount_homework = map(int, input().split())
a = map(int, input().split())
schedule_hw = list(a)

need_days_hw = 0

for i in schedule_hw:
    need_days_hw += i


if days_summer_vacation > need_days_hw:
    print(days_summer_vacation - need_days_hw)
elif days_summer_vacation == need_days_hw:
    print(0)
else:
    print(-1)