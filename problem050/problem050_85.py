#coding:utf-8
#1_5_B 2015.4.1
while True:
    length,width = map(int,input().split())
    if (length,width) == (0,0):
        break

    for i in range(length):
        for j in range(width):
            if j == width - 1:
                print('#')
            elif i == 0 or i == length - 1 or j == 0:
                print('#', end='')
            else:
                print('.', end='')
    print()