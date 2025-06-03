n = int(input())
a = list(map(int, input().split()))

m = 1
count = 0
for i in range(n):
    if a[i] != m:
        count += 1
    else:
        m += 1
print(count if count < n else -1)