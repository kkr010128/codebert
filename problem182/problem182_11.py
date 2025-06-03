n, k, c = map(int, input().split())
s = input()

bound_to_work = [0] * n

def get_days(s):
    days = [0] * n
    changes = [0] * n
    last_day = -1
    ndays = 0
    for i in range(n):
        if (last_day == -1 or i - last_day > c) and s[i] == 'o':
            ndays += 1
            last_day = i
            changes[i] = 1
        days[i] = ndays
    return days

ldays = get_days(s)
rdays = get_days(s[::-1])[::-1]


for i in range(n):
    lchanges = (i > 0 and ldays[i] != ldays[i - 1] or i == 0)
    rchanges = i == n - 1 or rdays[i + 1] != rdays[i]
    if  lchanges and rchanges and ldays[i] + rdays[i] == k + 1:
        bound_to_work[i] = 1

for i, f in enumerate(bound_to_work):
    if f:
        print(i + 1)
