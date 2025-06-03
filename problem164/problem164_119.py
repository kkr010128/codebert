import math
a,b,c,d = map(int,input().split(" "))
taka = math.ceil(c/b)
aoki = math.ceil(a/d)

if taka <= aoki:
    print("Yes")
else:
    print("No")