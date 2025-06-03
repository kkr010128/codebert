X = int(input())
flag = 0
if X == 2 or X == 3:
    flag = 1
    print(X)
while flag == 0 :
    for i in range(2,int(X**0.5)+1):
        if X%i == 0:
            X += 1
            break
        else:
            if i == int(X**0.5):
                flag = 1
                print(X)