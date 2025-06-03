#coding:utf-8
#1_5_C 2015.4.1
while True:
    length,width = map(int,input().split())
    if length == width == 0:
        break

    for i in range(length):
        for j in range(width):
            if (i + j) % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()