X,Y = map(int,input().split())
flag = 0
for a in range(X+1):
    b = X-a
    if 2*a+4*b == Y:
        print("Yes")
        flag = 1
        break
if flag == 0:
    print("No")