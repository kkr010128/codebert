num1 = int(input())
num = (int(x) for x in input().split())

count = 0

for i, name in enumerate(num):
    if i % 2 == 0:
        if name % 2 == 1:
            count = count + 1

print(count)