x=int(input())
a=0
while True:
    for b in range(10**3):
        if a**5-b**5==x:
            print(a,b)
            exit()
        elif a**5+b**5==x:
            print(a,-b)
            exit()
        elif -a**5+b**5==x:
            print(-a,-b)
            exit()
    a+=1