x = []
y = []
for i in range(2):
    x1,y1=[int(i) for i in input().split()]
    x.append(x1)
    y.append(y1)

if x[0]!=x[1]:
    print(1)
else:
    print(0)
