days = input()
consecutive_days = 0
max_days = 0

if 'R' in days:
    max_days = 1
    consecutive_days = 1

for weather in range(len(days) - 1):
    if days[weather] == days[weather + 1] and days[weather] == 'R':
        consecutive_days += 1
        if consecutive_days > max_days:
            max_days = consecutive_days

print(max_days)