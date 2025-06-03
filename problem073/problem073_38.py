n = int(input())

total = 0
for i in range(1, n + 1):
    j = n // i
    if n % i == 0:
        j -= 1
    total += j

print(total)

