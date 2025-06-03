x = int(input())
c = 1
while True:
    if c*100 <= x <= c*105:
        print(1)
        break

    if c*100 > x:
        print(0)
        break
    c += 1