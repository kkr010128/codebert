x = int(input())
for a in range(1001):
    for b in range(1001):
        if (a**5)-(b**5)==x:
            print(a,b)
            exit()
        if (a**5)+(b**5)==x:
            print(a,-1*b)
            exit()
        if (b**5)-(a**5)==x:
            print(-1*a,-1*b)
            exit()
