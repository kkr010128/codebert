a,b,n = map(int,input().split()) 

x=min(n,b-1)

ans = (int(a*x/b) - a * int(x/b))

print(ans)