x,y,z = map(int,input().split())

a,b,c = x,y,z
a,b = b,a
a,c = c,a

print(a,b,c)
