a,b,c=map(int,input().split())
x = 0
y = 0
for i in range(a):
    x = x + c
    y = y + b
    if a <= y:
        print(x)
        break