n = int(input())
a = list(map(int, input().split()))

sum = 0
k = a[0]

for i in range(n - 1):
    if k >= a[i + 1]:
        sum += k - a[i + 1]
    else:
        k = a[i + 1]

print(sum)
