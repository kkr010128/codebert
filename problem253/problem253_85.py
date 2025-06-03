n,a,b = map(int,input().split())
if (a-b)%2 == 0:
    print(abs(a-b)//2)
else:
    if abs(a-1) <= abs(n-b):
        # b -= abs(a-1)
        if (a-b)%2 == 1:
            b -= 1
            print(abs(a-1)+abs(a-b)//2+1)
        else:
            print(abs(a-1)+abs(a-b)//2)
    else:
        # a += abs(n-b)
        if (a-b)%2 == 1:
            # b += 1
            a += 1
            print(abs(n-b)+abs(a-b)//2+1)
        else:
            print(abs(n-b)+abs(a-b)//2)

