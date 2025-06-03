loop = int(raw_input())
taro = []
hanako = []
taro_score = 0
hanako_score = 0
for i in range(loop):
    t, h = raw_input().split()
    taro += [t]
    hanako += [h]

for t, h in zip(taro,hanako):
    if t < h:
        hanako_score += 3
    if t > h:
        taro_score += 3
    if t == h:
        taro_score += 1
        hanako_score += 1
print "%d %d" % (taro_score, hanako_score)