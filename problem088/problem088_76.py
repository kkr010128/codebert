N = int(input())
height = [int(i) for i in input().split()]
step = 0
for i, h in enumerate(height):
    if i == 0:
        pre = h
    else:
        if h < pre:
            step += (pre - h)
            pre = pre
        else:
            step += 0
            pre = h
print(step)