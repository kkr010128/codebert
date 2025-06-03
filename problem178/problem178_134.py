x,y,z = map(int,input().split())
temp = x
x = y
y = temp
temp = x
x = z
z = temp
print(x,y,z)