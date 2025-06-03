x,y = map(int,input().split())
m = 10**9+7
n = (x+y)//3
c = 0
if x*0.5 <= y <= 2*x and (x+y)%3 == 0:
    r = x - n
    c = 1
    for i in range(1,r+1):
        c *= (n-i+1) % m
        c *= pow(i,m-2,m)
        c = c % m
else:
    ans = 0
print(c)