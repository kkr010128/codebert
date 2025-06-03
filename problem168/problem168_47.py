n,m=map(int,input().split())
a =map(int,input().split())
x = sum(a)
if x > n:
    print('-1')



else:
    print(n-x)