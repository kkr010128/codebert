n = int(input())
taro = 0
hana = 0
for c in range(0,n):
    word = input().split(' ')
    taro_w, hana_w = word[0], word[1]
    word.sort()
    if word[0] == word[1]:
        taro += 1
        hana += 1
    elif taro_w == word[0]:
        hana += 3
    else:
        taro += 3
print("%d %d" % (taro, hana))