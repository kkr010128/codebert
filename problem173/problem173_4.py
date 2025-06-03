N = int(input())

SUM = 0

for i in range(1, N + 1):
    if i % 3 != 0:
        if i % 5 != 0:
            SUM += i

print(SUM)