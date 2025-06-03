cnt = int(input())
taro = 0
hanako = 0
for i in range(cnt):
    li = list(input().split())
    if li[0]>li[1]:
        taro +=3
    elif li[0]==li[1]:
        taro +=1
        hanako +=1
    else:
        hanako +=3
print(taro,hanako)
