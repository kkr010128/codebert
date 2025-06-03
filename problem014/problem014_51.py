n = int(input()) - 1
a = list(map(int, input().split()))

count = 0
flag  = 1

while flag:
    flag = 0
    j    = 0
    for i in range( n, j, -1 ):
        if a[i] < a[i-1]:
            t = a[i]
            a[i] = a[i-1]
            a[i-1] = t
            count += 1
            flag = 1
        j += 1

print(*a)
print(count)