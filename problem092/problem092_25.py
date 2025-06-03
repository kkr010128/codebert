x,k,d = list(map(int,input().split()))
x = abs(x)
point =x % d
num = x//d
if num<k:
    rest = k - num
    if rest%2==0:
        pass
    else:
        point = d -point
else:
    point = x - k*d
print(point)