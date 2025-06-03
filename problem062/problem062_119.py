# coding: utf-8
while True:
    a = input()
    if a == '0':
        exit()
    else:
        print(sum(list(map(int, a))))

