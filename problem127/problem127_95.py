x,y = map(int,input().split())

if 2*x <= y and y <= 4*x and (4*x - y) % 2 == 0:
    print("Yes")
else:
    print("No")