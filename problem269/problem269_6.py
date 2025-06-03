import numpy as np
t1,t2 = map(int, input().split())
a1,a2 = map(int, input().split())
b1,b2 = map(int, input().split())
# まず大きい方にswap
if a1 <= b1:
    a1,b1 = b1,a1
    a2,b2 = b2,a2

# t1での距離
x1 = a1*t1 - b1*t1
# t2での距離
x2 = x1 + a2*t2 - b2*t2
if x2 == 0:
    print("infinity")
elif x2 > 0:
    print(0)
else:
    ans =  int(np.ceil(x1/abs(x2))*2)
    if x1 % abs(x2) != 0:
        ans -= 1
    print(ans)