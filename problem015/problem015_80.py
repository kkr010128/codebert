n = int(input())
a = [int(i) for i in input().split()]
counter = 0
for i in range(n):
    minj = i
    for j in range(i, n):
        if a[j] < a[minj]:
            minj = j
    if minj != i:
        a[i], a[minj] = a[minj], a[i]
        counter += 1
print(*a)
print(counter)

