a, b, c, d = map(int,input().split())

x = a*c
y = b*d
z = a*d
w = b*c
print(max(x,y,z,w))