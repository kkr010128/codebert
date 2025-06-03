n = int(input())
a =[]
a = list(input().split())
for i in range(len(a)):
    a[i] = int(a[i])

if n < 0 or n > 10000:
    pass
else:
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    print(min(a), max(a), sum)