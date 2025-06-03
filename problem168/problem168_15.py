n,m = map(int,input().split())
a = map(int,input().split())
x = n-sum(a) 
if x >= 0:
    print(x)
else:
    print(-1)