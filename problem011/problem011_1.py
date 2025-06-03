x , y = map(int,input().split())

def GCD(x,y):
    while y > 0:
        x ,y = y , x %y
    else:
        return x

ans = GCD(x,y)
print(ans)