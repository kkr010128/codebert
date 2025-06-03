x = int(input())
k = []
for i in range(1, x + 1):
    y = i
    if i % 3 == 0:
        k.append(i)
    else:
        while True:
            if y % 10 == 3:
                k.append(i)
                break
            else:
                if y <= 10:
                    break
                else:
                    y //= 10

print(' '+ ' '.join([str(x) for x in k]))
