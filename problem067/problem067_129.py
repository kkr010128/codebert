taro = 0
hanako = 0
n = int(input())
for _ in range(n):
    taro_card, hanako_card = input().split()
    if taro_card > hanako_card:
        taro += 3
    elif taro_card < hanako_card:
        hanako += 3
    else:
        taro += 1
        hanako += 1
print(taro, hanako)