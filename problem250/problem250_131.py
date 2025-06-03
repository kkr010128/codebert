X = int(input())
while True:
    i = 2
    while i * i <= X:
        if X % i == 0:
            break
        i += 1
    else:
        print(X)
        break
    X += 1