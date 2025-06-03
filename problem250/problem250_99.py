X = int(input())-1
flag = True

while True:
    X += 1
    flag = True
    for j in range(2, int(X**0.5) +1):
        if X % j == 0:
            flag = False
            break
    if flag :
        print(X)
        break