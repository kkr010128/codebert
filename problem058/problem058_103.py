while True:
    count = 0
    n,x = map(int, input().split())
    if n == x == 0:
        break
    for i in range(1,n-1):
        for j in range(i+1,n):
            if ((x-i-j) > j) and (x-i-j) <= n:
                count += 1
    print(count)
