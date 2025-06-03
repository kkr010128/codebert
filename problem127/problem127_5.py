import sys
X,Y = map(int,input().split())
if Y %2 == 1:
    print("No")
    sys.exit()
if (X * 2 <= Y) and (X * 4 >= Y):
    print("Yes")
else:
    print("No")