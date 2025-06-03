n = int(input())
sum = 0
for _ in range(n):
    a = int(input())
    if a == 2:
        continue
    for i in range(a):
        x = i + 2
        if a%x == 0:
            sum += 1
            break
        if x > a ** 0.5:
            break
print(n - sum)

