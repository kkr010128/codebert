n = int(input())
a = [int(x) for x in input().split()]
result = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j +1 , n):
            if a[i] != a[j] and a[i] != a[k] and a[j] != a[k]:
                if a[i] + a[j] > a[k] and a[i] + a[k] > a[j] and a[j] + a[k] > a[i]:
                    result += 1
print(result)