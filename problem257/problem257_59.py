n = int(input())
a = list(map(int, input().split()))

if 1 in a:
    num = 1
    for i in range(n):
        if a[i] == num:
            a[i] = 0
            num += 1
        else:
            a[i] = 1
    print(sum(a))
else:
    print(-1)