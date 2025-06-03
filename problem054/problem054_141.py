# coding:utf-8

# ????????????
s = [False] * 13
# ?????????
h = [False] * 13 
# ?????????
c = [False] * 13
# ?????????
d = [False] * 13

T = {'S':s, 'H':h, 'C':c, 'D':d}

# ??\???
n = int(input())
for i in range(n):
    suit, num = input().split()
    num = int(num)
    T[suit][num-1] = True

for v in range(13):
    if not(T['S'][v]):
        print('S', v + 1)
for v in range(13):
    if not(T['H'][v]):
        print('H', v + 1)
for v in range(13):
    if not(T['C'][v]):
        print('C', v + 1)
for v in range(13):
    if not(T['D'][v]):
        print('D', v + 1)