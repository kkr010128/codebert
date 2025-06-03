a, b ,c = [int(i) for i in input().split()]

total = 0
for d in range(a, b + 1):
    if c % d == 0:
        total += 1

print(total)