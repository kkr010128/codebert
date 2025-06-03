X = int(input())
for i in range(X, 9999999999999999):
    flag = 1
    for j in range(2, X//2 +1):
        if i % j == 0:
            flag = -1
            break
    if X == 2:
        print(2)
        break
    elif X == 3:
        print(3)
        break
    elif flag == 1:
        print(i)
        break