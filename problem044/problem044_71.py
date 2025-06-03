num = [int(x) for x in input().split() if x.isdigit()]
count = 0
for i in range(num[0], num[1]+1):
    if num[2] % i == 0:
        count += 1
print(count)