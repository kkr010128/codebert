n, a, b = map(int,input().split())
tmp = abs(a-b)

if tmp%2 == 0:
    print(tmp//2)
else:
    x = a-1
    y = n-b
    print(min(x,y)+1+((b-a-1)//2))
