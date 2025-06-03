X,Y=map(int, input().split())
v = [300000, 200000, 100000]
x = 0
y = 0
if X <= 3:
    x = int(v[X-1])
if Y <= 3:
    y = int(v[Y-1])
print(int(x + y + ((X==1) & (Y==1)) * 400000))
