n,m = input().split()

n=int(n)
m=float(m)*100+0.5
m=int(m)

ans = int(n*m//100)

print(ans)