n = int(input())
debt = 100000

for i in range(n):
    debt *= 1.05
    if debt % 1000 > 0:
        tmp = debt % 1000
        debt -= tmp
        debt += 1000

print(int(debt))