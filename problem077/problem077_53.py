a,b,c,d = (int(x) for x in input().split())
ans = max(a*c,a*d,b*c,b*d)
print(ans)