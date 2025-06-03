import sys

l = []
for i in sys.stdin:
    l.append(i.split())

taro = 0
hanako = 0
for i in range(1,len(l)):
    if l[i][1] > l[i][0]:
        hanako += 3
    elif l[i][0] > l[i][1]:
        taro += 3
    else:
        hanako += 1
        taro += 1

print(taro,hanako)
