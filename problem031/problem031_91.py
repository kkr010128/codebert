while True:
    n = int(input())
    if n == 0:
        break
    x = tuple(map(float, input().strip().split()))
    y = (sum(x)/n)**2
    z = sum(map(pow, x, (2 for i in range(n))))/n
    print((z-y)**0.5)