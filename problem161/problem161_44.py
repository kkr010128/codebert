a, b, n = [int(x) for x in input().split()]

n = min(n,b-1)
x = max(0,n-a-a-a-a)

s = -a

for i in range(x,n+1):
    s = max(s,(a*i//b)-a*(i//b))



print(s)
