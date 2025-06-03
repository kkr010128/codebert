x,k,d=map(int,input().split())
x = abs(x)
tmp = min(k, x//d);
k -= tmp
x -= tmp * d
if(k%2 == 0):print(x)
else:print(d-x)