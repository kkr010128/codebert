n=int(input())
taro=0
hanako=0
for i in range(n):
    t,h=map(str,input().split())
    if t>h:
        taro += 3
    elif h>t:
        hanako += 3
    else:
        taro += 1
        hanako += 1
print(taro,hanako)
