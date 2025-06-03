while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    m = sum(s)/n
    a2 = 0.0
    for i in range(n):
        a2 += (s[i] - m)**2
    a = (a2/n)**0.5
    print(a)