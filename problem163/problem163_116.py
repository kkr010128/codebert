o   = ['unsafe','safe']
s,w = map(int,input().split())
f   = 0


if w >= s:
    f = 0
else:
    f = 1

print(o[f])