while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    else:
        counter = 0
        for a in range(1,(x // 3)):
            for c in range ((x//3)+1,n+1):
                b = x - a - c
                if a < b < c:
                    counter += 1
        print(counter)