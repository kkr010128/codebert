n = int(input())
c = input()
count = 0

i, j = 0, n - 1
if c.count('W') == 0:
    count=0
elif c.count('R') == 0:
    count = 0
else:
    white_cnt = []
    red_cnt = []
    for i in range(n):
        if c[i] == 'W':
            white_cnt.append(i)
        else:
            red_cnt.append(i)
    while 1:
        white_num = white_cnt.pop(0)
        red_num = red_cnt.pop()
        if white_num < red_num:
            count += 1
        if len(white_cnt) == 0:
            break
        if len(red_cnt) == 0:
            break
print(count)
