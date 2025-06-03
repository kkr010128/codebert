from collections import deque

s  = input()
q = int(input())

#flag=0 でleft, flag=1でrightが先頭
flag = 0
cnt = 0
d  = deque(s)

for _ in range(q):
    lis = list(input().split())
    if lis[0] == "1":
        if flag:
            flag = 0
        else:
            flag = 1
        cnt += 1
    else:
        if lis[1] == '1':
            if flag:
                d.append(lis[2])
            else:
                d.appendleft(lis[2])
        else:
            if flag:
                d.appendleft(lis[2])
            else:
                d.append(lis[2])


d = list(d)
if cnt % 2 != 0:
    d = d[::-1]


print(''.join(d))