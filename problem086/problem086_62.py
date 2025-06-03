n,x,t = map(int,input().split())
ans = int((n+x-1)/x)
ans *= t
print(ans)