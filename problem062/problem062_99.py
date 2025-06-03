#coding:utf-8
#1_8_B 2015.4.7
while True:
    number = input()
    if number == '0':
        break
    print(sum(int(i) for i in number))