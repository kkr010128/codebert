n = int(input())
count = 0

for i in range(1,10):
    for j in range(1,10):
        if n == i*j:
            count += 1

        else:
            pass
print(['No','Yes'][count != 0])