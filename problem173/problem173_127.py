n = int(input())
sum = 0
for i in range(n + 1):
    if i % 3 != 0 and i % 5 != 0 and i % 15 != 0:
        sum += i
print(sum)