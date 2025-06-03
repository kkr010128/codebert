X = int(input())
for i in range(-201, 201):
    done = False
    for j in range(-201, 201):
        if i ** 5 - j ** 5 == X:
            print(i, j)
            done = True
            break
    if done:
        break