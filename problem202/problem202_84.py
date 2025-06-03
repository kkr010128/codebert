n,a,b = map(int, input().split())
g = n//(a+b)
k = n-(a+b)*g
if k >= a:
    print(a+a*g)
else:
    print(a*g + k)