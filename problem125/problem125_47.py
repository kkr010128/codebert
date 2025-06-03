x = int(input())
a = 360
for _ in range(360):
    if a%x == 0:
        print(a//x)
        break
    else:
        a += 360