turn = int(input())
tp, hp = 0, 0
for i in range(turn):
    t, h = input().split()
    if t == h:
        tp += 1
        hp += 1
    elif t > h:
        tp += 3
    elif t < h:
        hp += 3
print(tp, hp)
