num1, num2, num3 = (int(x) for x in input().split())
count = 0

for i in range(num1, num2+1):
    if i % num3 == 0:
        count = count + 1

print(count)