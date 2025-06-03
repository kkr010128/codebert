n = int(input())
a = [int(i) for i in input().split()]

num = 0

is_swapped = True
i = 0
while is_swapped:
    is_swapped = False
    for j in range(n-1, i, -1):
        if a[j] < a[j-1]:
            tmp = a[j]
            a[j] = a[j-1]
            a[j-1] = tmp
            is_swapped = True
            num += 1
    i += 1

print(' '.join([str(i) for i in a]))
print(num)
