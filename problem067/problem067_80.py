n = int(input())
tp = hp = 0
while n:
    t, h = input().split()
    if t > h:
        tp += 3
    elif t < h:
        hp += 3
    else:
        tp += 1
        hp += 1
    n -= 1
print(tp, hp)