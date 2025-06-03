debt = 100000.0

a = int(input())
for i in range(a):
    debt = debt * 1.05
    if(debt % 1000):
        debt = (debt // 1000) * 1000 + 1000
print(int(debt))

