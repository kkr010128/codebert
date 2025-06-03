n = input()
a = map(int, raw_input().split())
min = a[0]
max = a[0]
sum = 0
for i in range(n):
    if min > a[i]:
        min = a[i]
    if max < a[i]:
        max = a[i]
    sum += a[i]
print min, max, sum