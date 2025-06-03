n = int(input())
a = list(map(int, input().split()))

last  = 0
count = 0
flag  = True

while flag:
    flag = False
    for i in range( n-1, last, -1 ):
        if a[i] < a[i-1]:
            t = a[i]
            a[i] = a[i-1]
            a[i-1] = t
            count += 1
            flag = True
    last += 1

print(*a)
print(count)