a,b,c,d = map(int,input().split())
s = max(max(a*c,a*d),max(b*c,b*d))
print(s)