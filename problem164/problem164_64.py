a, b, c, d = map(int,input().split())
flag = True
while a > 0 and c > 0:
    c -= b
    if c <= 0:
        flag = True
        break
    a -= d
    if a <= 0:
        flag = False
        break
if flag:
    print('Yes')
else:
    print('No')