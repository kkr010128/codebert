n,a,b=map(int,input().split())
s=n//(a+b)
w=n%(a+b)
if w<=a:
    print(s*a+w)
else:
    print(s*a+a)