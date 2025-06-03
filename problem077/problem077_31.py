a,b,c,d = map(int,input().split())
e = a*c
f = a*d
g = b*c
h = b*d
xy =[e,f,g,h]
print(int(max(xy)))