x = int(input())

flag = 0

for a in range(x):
    b5 = a**5 - x
    for b in range(120):
        if abs(b5) == int(b**5):
            if b5 < 0:
                b = -b
            flag = 1
            break
    if flag:
        break

print(a, int(b))
