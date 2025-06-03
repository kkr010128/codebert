while True:
    n = int(input())
    if n == 0:
        break

    s = list(map(int,input().split()))
    m = 0
    sum = 0
    for i in range(n):
        sum += s[i]
    m = sum/n

    tmp = 0
    for i in range(n):
        tmp += (s[i]-m)**2
    print((tmp/n)**0.5)