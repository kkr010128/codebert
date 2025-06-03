n = int(input())

for i in range(n):
    a,b,c = map(int,input().split(" "))
    if a**2 == b**2 + c**2:
        print("YES")
    elif b**2 == a**2 + c**2:
        print("YES")
    elif c**2 == a**2 + b**2:
        print("YES")
    else:
        print("NO")