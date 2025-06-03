while True:
    y,x = [int(i) for i in input().split()]
    if x==0 and y==0:
        break
    for i in range(y):
        if i%2:
            for j in range(x):
                if j%2:
                    print('#' ,end='')
                else:
                    print('.' ,end='')
            print()
        else:
            for j in range(x):
                if j%2:
                    print('.' ,end='')
                else:
                    print('#' ,end='')
            print()
    print()