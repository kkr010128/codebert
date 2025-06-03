while(1):
    n, x = map(int, input().split())

    if n == 0 and x == 0:
        break

    count = 0
    for i in range(1, n-1):
        if i*3 >= x:
            break
        for j in range(i+1, n):
            if i+2*j >= x:
                break
            if x-i-j <= n:
                count += 1

    print(count)