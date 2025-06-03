n = int(input())

total = 0

for i in range(1, 10**6 + 1):
    for j in range(1, 10**6 + 1):
        m = n - i * j
        if m > 0:
            total += 1
        else:
            break

print(total)