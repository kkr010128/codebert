N,R = map(int,input().split())
ans = lambda n,r: r if n>=10 else r + 100*(10 - n)
print(ans(N,R))