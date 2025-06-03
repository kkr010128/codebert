X,Y=map(int, input().split())
v1 = [300000, 200000, 100000]
v2 = [300000, 200000, 100000]
x = 0
y = 0
if X <= 3:
    x = int(v1[X-1])
if Y <= 3:
    y = int(v2[Y-1])
if ((X==1) & (Y==1)):
    print(int(x + y + 400000))
else:
    print(int(x + y))