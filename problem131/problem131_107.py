A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
diff_dist = B - A
diff_v = V - W
flag = False
if diff_v == 0:
    if diff_dist == 0:
        flag = True
elif diff_dist == 0:
    flag = True
else:
    if diff_v > 0:
        t = abs(diff_dist) / diff_v
        if t <= T:
            flag = True
if flag:
    print('YES')
else:
    print('NO')