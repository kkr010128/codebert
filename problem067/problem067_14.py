tp = hp = 0
for i in range(int(input())):
    taro, hana = map(list, input().split())
    short = min(len(taro), len(hana))
    result = 0
    for k in range(short):
        if ord(taro[k]) != ord(hana[k]):
            result = ord(taro[k]) - ord(hana[k])
            break
    if not result:
        if len(taro) < len(hana):
            result = -1
        elif len(taro) > len(hana):
            result = 1
    if result > 0:
        tp += 3
    elif result < 0:
        hp += 3
    else:
        tp += 1
        hp += 1
print(tp, hp)
