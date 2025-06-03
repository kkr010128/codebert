
a,b=map(int,input().split())

c=a>b

print(str(b if c else a)*(a if c else b))
