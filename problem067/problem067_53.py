taro_point = 0
hanako_point = 0
N = int(input())
for _ in range(N):
    taro,hanako = input().split()
    list = [taro,hanako]
    list_new = sorted(list)
    if taro == hanako:
        taro_point += 1
        hanako_point += 1
    elif list_new[1] == hanako:
        hanako_point +=3
    elif list_new[1] == taro:
        taro_point += 3
print(str(taro_point),str(hanako_point))
