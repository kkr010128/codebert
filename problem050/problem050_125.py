#coding:utf-8
#1_5_B 2015.4.1
while True:
    length,width = map(int,input().split())
    if length == width == 0:
        break
    print('#' * width)
    print(('#' + '.' * (width - 2) + '#\n') * (length - 2),end='')
    print('#' * width)
    print()