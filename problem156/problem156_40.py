X = int(input())
flag = 0

for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        if a**5 - b**5 == X:
            print(a, b)
            flag = 1
            break
    if flag == 1:
        break