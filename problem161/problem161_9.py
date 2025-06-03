a,b,n = map(int, input().split())
yuka = lambda a,b: (a-(a%b))//b

x = min(n,b-1)
score = yuka(a*(x%b),b)
ans = score

print(ans)