
week = int(input())
debt = 100000

for i in range(week):
    debt += debt * 0.05
    thousand = int(debt / 1000)
    coin = debt - thousand * 1000
    if 0 < coin:
        thousand += 1 
    debt = thousand * 1000

print(debt)