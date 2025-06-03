n,x,d = map(int, input().split())
if n%x == 0:
    print(n//x*d)
else:
    print((n//x+1)*d)