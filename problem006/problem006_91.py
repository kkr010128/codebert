n = int(input())
debt = 100000
for i in range(n):
    debt *= 1.05
    if debt%1000 != 0:
        debt += 1000 - debt%1000
print(int(debt))