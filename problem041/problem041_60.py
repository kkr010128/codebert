# coding: utf-8
# Here your code !
W, H , x ,y ,r = list(map(int, input().split()))

t1_x = x + r
t1_y = y + r

t2_x = x - r
t2_y = y - r

if 0 <= t1_x <= W and 0 <= t1_y <= H and 0 <= t2_x <= W and 0 <= t2_y <= H:
    print("Yes")
else:
    print("No")