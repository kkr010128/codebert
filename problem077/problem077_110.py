a,b,c,d = map(int,input().split())
k = max(a*c,b*d)
l = max(a*d,b*c)
print(max(k,l))